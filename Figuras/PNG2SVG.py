import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import glob
from pathlib import Path

# 1. Configuración de ruta
ruta_carpeta = r"C:\Users\pfran\Documents\UNAB\Workshop Gliomas 2026\Figuras"

# 2. Buscar archivos PNG (detecta tanto .png como .PNG)
extensiones = ('*.png', '*.PNG')
archivos = []
for ext in extensiones:
    archivos.extend(glob.glob(os.path.join(ruta_carpeta, ext)))

if not archivos:
    print(f"No se encontraron archivos PNG en: {ruta_carpeta}")
else:
    print(f"Se encontraron {len(archivos)} archivos. Iniciando conversión...\n")
    
    for img_path in archivos:
        try:
            # Cargar la imagen para obtener dimensiones
            img = mpimg.imread(img_path)
            alto_px, ancho_px = img.shape[:2]
            
            # 3. Configuración de dimensiones reales
            # Definimos un DPI estándar para el cálculo (no afecta la calidad final del SVG)
            dpi = 100
            ancho_pulgadas = ancho_px / dpi
            alto_pulgadas = alto_px / dpi
            
            # Crear figura con el tamaño exacto de la imagen
            fig = plt.figure(figsize=(ancho_pulgadas, alto_pulgadas), dpi=dpi)
            
            # Configurar ejes para que ocupen todo el lienzo (sin bordes blancos)
            ax = plt.Axes(fig, [0., 0., 1., 1.])
            ax.set_axis_off()
            fig.add_axes(ax)
            
            # Mostrar imagen manteniendo la relación de aspecto original
            ax.imshow(img, aspect='equal')
            
            # 4. Definir nombre de salida con pathlib (más seguro)
            path_obj = Path(img_path)
            nombre_svg = path_obj.with_suffix('.svg')
            
            # 5. Forzar actualización: eliminar el SVG si ya existe
            if nombre_svg.exists():
                nombre_svg.unlink()
            
            # Guardar como SVG
            # transparent=True mantiene el fondo transparente si el PNG lo era
            plt.savefig(str(nombre_svg), format='svg', bbox_inches='tight', pad_inches=0, transparent=True)
            plt.close(fig)
            
            print(f"ÉXITO: {path_obj.name} -> {nombre_svg.name} ({ancho_px}x{alto_px} px)")
            
        except Exception as e:
            print(f"ERROR al procesar {os.path.basename(img_path)}: {e}")

print("\n Proceso terminado. Si no ves cambios en la fecha, presiona F5 en la carpeta.")