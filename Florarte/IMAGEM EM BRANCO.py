from PIL import Image
import imagehash
import os
import sys # Nova importação para manipular a saída do console

# --- Funções de hash ---
def comparar_hashes(hash1, hash2):
    """Compara dois hashes de imagem."""
    return str(hash1) == str(hash2)

def calcular_hash_imagem(caminho_imagem):
    """Calcula o hash médio de uma imagem."""
    try:
        with Image.open(caminho_imagem) as imagem:
            return imagehash.average_hash(imagem)
    except FileNotFoundError:
        # Não precisa imprimir erro aqui, pois já verificamos antes de chamar
        return None
    except Exception as e:
        # print(f"Erro ao calcular hash de {caminho_imagem}: {e}") # Descomente para depuração
        return None

# --- Função principal de categorização de imagens ---
def categorizar_imagens_por_hash(caminho_pasta, hash_aguardando_imagem, hash_em_branco):
    """
    Categoriza todas as imagens JPG em uma pasta (e subpastas)
    com base em dois hashes de referência, exibindo um progresso em porcentagem.

    Retorna 4 listas: imagens localizadas, aguardando imagem, em branco e com erro.
    """
    imagens_localizadas = []
    imagens_aguardando_imagem = []
    imagens_em_branco = []
    imagens_com_erro = []

    print(f"\nIniciando varredura na pasta: {caminho_pasta}")

    # PRIMEIRA PASSAGEM: Contar todos os arquivos JPG e coletar seus caminhos
    all_jpg_files = []
    for root, _, files in os.walk(caminho_pasta):
        for file in files:
            if file.lower().endswith('.jpg'):
                all_jpg_files.append(os.path.join(root, file))

    total_files_to_process = len(all_jpg_files)
    
    if total_files_to_process == 0:
        print("Nenhum arquivo JPG encontrado na pasta especificada.")
        return [], [], [], [] # Retorna listas vazias

    processed_count = 0
    print(f"Total de arquivos JPG a processar: {total_files_to_process}")

    # SEGUNDA PASSAGEM: Processar cada arquivo e atualizar o progresso
    for caminho_arquivo in all_jpg_files:
        processed_count += 1
        nome_imagem_sem_ext = os.path.splitext(os.path.basename(caminho_arquivo))[0]
        
        # Calcular e exibir a porcentagem de progresso
        percentage = (processed_count / total_files_to_process) * 100
        # Use \r para retornar ao início da linha e sobrescrever
        sys.stdout.write(f"\rProcessando: {processed_count}/{total_files_to_process} ({percentage:.2f}%) - {nome_imagem_sem_ext} ")
        sys.stdout.flush() # Força a impressão imediata

        try:
            hash_atual = calcular_hash_imagem(caminho_arquivo)
            if hash_atual is None:
                imagens_com_erro.append(f'{nome_imagem_sem_ext} (Hash inválido ou arquivo corrompido)')
                continue

            if comparar_hashes(hash_aguardando_imagem, hash_atual):
                imagens_aguardando_imagem.append(nome_imagem_sem_ext)
            elif comparar_hashes(hash_em_branco, hash_atual):
                imagens_em_branco.append(nome_imagem_sem_ext)
            else:
                imagens_localizadas.append(nome_imagem_sem_ext)
        except Exception as e:
            imagens_com_erro.append(f'{nome_imagem_sem_ext} (Erro: {e})')
            # print(f"Erro ao processar {caminho_arquivo}: {e}") # Descomente para depuração de erros específicos

    sys.stdout.write("\n") # Garante uma nova linha após o progresso terminar
    sys.stdout.flush()

    return imagens_localizadas, imagens_aguardando_imagem, imagens_em_branco, imagens_com_erro

# --- Configurações e execução ---

# Caminho para a pasta onde as imagens serão pesquisadas (adapte este caminho)
# Exemplo local: caminho_pasta = r'C:\Users\SeuUsuario\MinhasImagensDeProduto'
caminho_pasta = r'R:\\'

# --- Defina os caminhos para suas imagens de exemplo para os hashes ---
# Imagem de exemplo para "aguardando imagem" (a que você já usava)
caminho_imagem_exemplo_aguardando = r'D:\56158.jpg'

# Imagem de exemplo para "em branco" (adicione o caminho para a sua imagem "em branco")
# EX: caminho_imagem_exemplo_em_branco = r'C:\Users\SeuUsuario\Imagens\imagem_padrao_em_branco.jpg'
caminho_imagem_exemplo_em_branco = r'D:\68461.jpg' # ADAPTE ESTE CAMINHO!

# --- Calcular os hashes das imagens de exemplo ---
print("Calculando hashes das imagens de exemplo...")
hash_aguardando_imagem = calcular_hash_imagem(caminho_imagem_exemplo_aguardando)
hash_em_branco = calcular_hash_imagem(caminho_imagem_exemplo_em_branco)

if hash_aguardando_imagem is None:
    print(f"Não foi possível calcular o hash da imagem de exemplo 'aguardando imagem'. Verifique o caminho: {caminho_imagem_exemplo_aguardando}")
    exit() # Sai do script se o hash principal não puder ser calculado

if hash_em_branco is None:
    print(f"Não foi possível calcular o hash da imagem de exemplo 'em branco'. Verifique o caminho: {caminho_imagem_exemplo_em_branco}")
    # Podemos continuar se a imagem em branco for opcional, ou sair como acima.
    # Por segurança, vou sair também se essa for crítica.
    exit()

print(f'Hash da imagem de exemplo "aguardando imagem": {hash_aguardando_imagem}')
print(f'Hash da imagem de exemplo "em branco": {hash_em_branco}')


# --- Executar a categorização ---
imagens_localizadas, imagens_aguardando_imagem, imagens_em_branco, imagens_com_erro = \
    categorizar_imagens_por_hash(caminho_pasta, hash_aguardando_imagem, hash_em_branco)


# --- Resumo dos resultados ---
total_processadas = len(imagens_localizadas) + len(imagens_aguardando_imagem) + len(imagens_em_branco) + len(imagens_com_erro)
total_localizadas = len(imagens_localizadas)
total_aguardando_imagem = len(imagens_aguardando_imagem)
total_em_branco = len(imagens_em_branco)
total_com_erro = len(imagens_com_erro)

resultado = f'--- Resumo da Categorização de Imagens ---\n'
resultado += f'Pasta Analisada: {caminho_pasta}\n'
resultado += f'Total de Imagens JPG Processadas: {total_processadas}\n'
resultado += f'-----------------------------------------\n\n'

resultado += f'Códigos de Imagens LOCALIZADAS ({total_localizadas}):\n'
resultado += f'{", ".join(imagens_localizadas)}\n\n' # Use join para melhor visualização

resultado += f'Códigos de Imagens AGUARDANDO IMAGEM ({total_aguardando_imagem}):\n'
resultado += f'{", ".join(imagens_aguardando_imagem)}\n\n'

resultado += f'Códigos de Imagens EM BRANCO ({total_em_branco}):\n'
resultado += f'{", ".join(imagens_em_branco)}\n\n'

if imagens_com_erro:
    resultado += f'Códigos de Imagens COM ERRO NO PROCESSAMENTO ({total_com_erro}):\n'
    resultado += f'{", ".join(imagens_com_erro)}\n\n'

print(resultado)

# --- Exportar resultados para arquivo de texto ---
# Caminho para salvar o arquivo de resultados (adapte este caminho)
caminho_arquivo_saida = r'C:\Users\drdc\Downloads\relatorio_imagens_em_branco_e_aguardando_imagem.txt'

try:
    with open(caminho_arquivo_saida, 'w', encoding='utf-8') as arquivo:
        arquivo.write(resultado)
    print(f"\nResultado exportado com sucesso para: {caminho_arquivo_saida}")
except Exception as e:
    print(f"\nErro ao exportar resultado para o arquivo: {e}")
