import os 
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS

def leer_metadatos_foto(ruta_foto):
    """
    Lee los metadatos EXIF de una foto y extraer información útil
    """
    try:
        imagen = Image.open(ruta_foto)

        exif_data = imagen.getexif()

        if exif_data is not None:
            print(f"\nFOTO: {os.path.basename(ruta_foto)}")
            print("=" * 50)
        
            print(f"Tamaño: {imagen.size[0]} x {imagen.size[1]} pixeles")
            print(f"Formato: {imagen.format}")

    except Exception as e:
        print(f"Error procesando la foto: {str(e)}")
    

if __name__ == "__main__":
    print("Analizador de metadatos de fotos")
    print("=" * 40)

    carpeta_test = "test_photos"

    if not os.path.exists(carpeta_test):
        print(f"Creando carpeta {carpeta_test}...")
        os.makedirs(carpeta_test)
        print("Copia algunas fotos en la carpeta 'test_photos' y ejecuta de nuevo")
    else:

        extensiones_validas = ('.jpg', '.jpeg', '.png', '.tiff', '.bmp')
        fotos = []

        for archivo in os.listdir(carpeta_test):
            if archivo.lower().endswith(extensiones_validas):
                fotos.append(os.path.join(carpeta_test, archivo))


        if fotos:
            print(f"Encontradas {len(fotos)} fotos(s):")
            for foto in fotos:
                leer_metadatos_foto(foto)
                print("-" * 40)

        else:
            print("No se encontraron fotos en 'test_photos'")


print("Análisis completado!")        