import os
from PIL import Image

def check_image_for_color(image_path, color, tolerance=20):
    try:
        # Abrir a imagem
        image = Image.open(image_path)

        # Definir as dimensões do recorte (canto inferior esquerdo)
        width, height = image.size
        obj_width, obj_height = 59, 59  # Tamanho da região que queremos verificar
        margin = 29  # Margem de distância do canto inferior esquerdo

        # Coordenadas para recortar o canto inferior esquerdo
        left = margin
        top = height - obj_height - margin
        right = left + obj_width
        bottom = top + obj_height

        # Recortar a região
        region = image.crop((left, top, right, bottom))

        # Verificar se a cor está presente na região
        pixels = list(region.getdata())
        match = all(
            abs(pixel[0] - color[0]) <= tolerance and
            abs(pixel[1] - color[1]) <= tolerance and
            abs(pixel[2] - color[2]) <= tolerance
            for pixel in pixels
        )

        return match
    except Exception as e:
        print(f"Erro ao processar a imagem: {e}")
        return False

# Função para checar várias imagens em um diretório
def check_images(image_list, directory_path, color):
    results = []
    for image_name in image_list:
        image_name_with_extension = f"{image_name}.jpg"
        image_path = os.path.join(directory_path, image_name_with_extension)

        # Verificar se o arquivo existe
        if not os.path.exists(image_path):
            results.append(f"{image_name_with_extension}: Arquivo não encontrado.")
            continue

        # Verificar a cor no canto inferior esquerdo
        if check_image_for_color(image_path, color):
            results.append(f"{image_name_with_extension}: Cor encontrada no canto inferior esquerdo!")
        else:
            results.append(f"{image_name_with_extension}: Cor não encontrada no canto inferior esquerdo.")

    return results

# Diretório fixo
directory_path = r"\\fas01wap\EntregaFA-DA"

# Lista manual de imagens (sem .jpg)
image_list = ["91352002"]

# Cor que você está procurando (RGB)
target_color = (150, 150, 150)  # Cor #969696

# Checar as características das imagens
resultado = check_images(image_list, directory_path, target_color)

# Exibir os resultados
for res in resultado:
    print(res)
