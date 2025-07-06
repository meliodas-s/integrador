from matplotlib.transforms import Affine2D
from matplotlib.path import Path
from matplotlib.collections import PatchCollection
import matplotlib.patches as patches
import numpy as np

# Miselaneos
from copy import deepcopy


class Vinculo:
    def __init__(self, nod, ang):

        # Datos para graficar
        self.nod = nod
        self.ang = ang
        self.dax = float(nod.loc['cox'])
        self.day = float(nod.loc['coy'])

    def print(self, ax, x=0, y=0, fi=0, c=1):
        """
        Insertar_Vinculo.
        Inserta una PathCollection en un Axes dado, con transformación:
        - traslación (x, y)
        - rotación (fi en radianes o grados)
        - escalado por factor c

        Parámetros:
            collection: PathCollection ya creada
            ax: objeto Axes donde se agregará
            x, y: coordenadas de traslación
            fi: ángulo de rotación (radianes)
            c: factor de escala

        Retorna:
            La colección modificada y agregada al gráfico.
        """
        x = self.dax
        y = self.day
        fi = np.radians(self.ang)

        # Punto pivot
        xp, yp = (0.5, 1)

        # Crear transformación
        trans = Affine2D()
        trans.translate(-xp, -yp)
        trans.scale(c)
        trans.rotate(fi)
        trans.translate(x, y)

        # Aplicar transformación y agregar al eje
        self.grafica = deepcopy(self.path)

        self.grafica.set_transform(trans + ax.transData)
        ax.add_collection(self.grafica)


class ViculoSeg(Vinculo):
    def __init__(self, nod, ang):
        super().__init__(nod, ang)

        # Primer triángulo
        verts1 = np.array([[0, 0], [1, 0], [0.5, 1], [0, 0]])
        codes1 = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.CLOSEPOLY]

        # Segundo triángulo desplazado
        verts2 = np.array([[-0.25, 0], [1.25, 0]])
        codes2 = [Path.MOVETO, Path.LINETO]

        # Base del apoyo
        verts3 = list()
        codes3 = list()
        for i in range(10):
            verts3.append([-0.27 + i*1.45/9, -0.2])
            verts3.append([-0.23 + i*1.45/9, 0])
            codes3.append(Path.MOVETO)
            codes3.append(Path.LINETO)

        # Eje circulo
        circle = patches.Circle((0.5, 1), 0.08)

        # Combinar
        verts = np.concatenate([verts1, verts2])
        verts = np.concatenate([verts, np.array(verts3)])
        codes = codes1 + codes2 + codes3

        # Crear path combinado
        combined_path = patches.PathPatch(Path(verts, codes))

        # Punto pivot
        xp, yp = (0.5, 1)

        # Convinacion final
        collection = PatchCollection(
            [combined_path, circle], facecolor='white', edgecolor='black', linewidth=1)

        # Llevar el pivot al origen
        trans = Affine2D()
        collection.set_transform(trans)

        self.path = collection


class ViculoPri(Vinculo):
    def __init__(self, nod, ang):
        super().__init__(nod, ang)

        # Primer triángulo
        verts1 = np.array([[0, 0.24], [1, 0.24], [0.5, 1], [0, 0.24]])
        codes1 = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.CLOSEPOLY]

        # Segundo triángulo desplazado
        verts2 = np.array([[-0.25, 0], [1.25, 0]])
        codes2 = [Path.MOVETO, Path.LINETO]

        # Base del apoyo
        verts3 = list()
        codes3 = list()
        for i in range(10):
            verts3.append([-0.27 + i*1.45/9, -0.2])
            verts3.append([-0.23 + i*1.45/9, 0])
            codes3.append(Path.MOVETO)
            codes3.append(Path.LINETO)

        # Eje circulo
        circle = patches.Circle((0.5, 1), 0.08)

        # Combinar
        verts = np.concatenate([verts1, verts2])
        verts = np.concatenate([verts, np.array(verts3)])
        codes = codes1 + codes2 + codes3

        # Crear path combinado
        combined_path = patches.PathPatch(Path(verts, codes))
        soporte = [combined_path, circle]

        # Creadno rueditas
        for i in range(int(1/0.24)):
            soporte.append(patches.Circle((0.14+i*0.24, 0.12), 0.12))

        # Convinacion final soportecoleccion
        sopcol = PatchCollection(
            soporte, facecolor='white', edgecolor='black', linewidth=1)

        self.path = sopcol


class viculoTer(Vinculo):
    def __init__(self, nod, ang):
        super().__init__(nod, ang)

        # Segundo triángulo desplazado
        verts2 = np.array([[-0.25, 0], [1.25, 0]])
        codes2 = [Path.MOVETO, Path.LINETO]

        # Rayas
        verts3 = list()
        codes3 = list()
        for i in range(10):
            verts3.append([-0.27 + i*1.45/9, -0.2])
            verts3.append([-0.23 + i*1.45/9, 0])
            codes3.append(Path.MOVETO)
            codes3.append(Path.LINETO)

        # Combinar
        verts = np.concatenate([verts2, verts3])
        codes = codes3 + codes2

        # Crear path combinado
        combined_path = patches.PathPatch(Path(verts, codes))
        soporte = [combined_path]

        # Convinacion final soportecoleccion
        vinc3er = PatchCollection(
            soporte, facecolor='grey', edgecolor='black', linewidth=1)

        self.path = vinc3er
