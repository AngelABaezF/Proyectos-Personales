from rembg import remove
from PIL import Image
import io

def quitar_fondo(imagen_entrada, imagen_salida):
    # Abrimos la imagen original
    with open(imagen_entrada, 'rb') as img_file:
        input_data = img_file.read()
    
    # Quitamos el fondo
    output_data = remove(input_data)
    
    # Guardamos la imagen sin fondo en PNG
    img_result = Image.open(io.BytesIO(output_data))
    img_result.save(imagen_salida, 'PNG')

# Ejemplo de uso
quitar_fondo("imagen_con_fondo.jpg", "imagen_sin_fondo.png")