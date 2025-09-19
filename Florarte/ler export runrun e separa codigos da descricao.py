import re
import pandas as pd

# 1. CAMINHOS DOS ARQUIVOS
# Caminho do arquivo Excel original
caminho_original = r"C:\Users\drdc\Downloads\Estúdio_-_Solicitações-2025-09-17-08h-27m-10s.xlsx"
# Nome do novo arquivo Excel que será criado
caminho_novo = r"C:\Users\drdc\Downloads\Estúdio_-_Solicitações_COM_CODIGOS.xlsx"

# 2. Regex para capturar os códigos
padrao = re.compile(r"\b\d{6,8}F?\b|\b\d{5}-\d{3}\b")

try:
    # 3. Ler a planilha inteira
    df = pd.read_excel(caminho_original)

    # 4. Checar se a 7ª coluna (Índice 6, Coluna G) existe
    if len(df.columns) > 6:
        coluna_alvo = df.columns[6]

        # 5. Função para extrair os códigos de cada célula
        def extrair_codigos(texto):
            if pd.isna(texto):
                return ""  # Retorna uma string vazia se a célula for nula
            # Garante que o conteúdo seja lido como texto antes de aplicar a regex
            codigos_encontrados = padrao.findall(str(texto))
            # Junta os códigos encontrados com uma vírgula
            return ", ".join(codigos_encontrados)

        # 6. Criar a nova coluna "Codigos_Extraidos"
        # O .apply() executa a função 'extrair_codigos' para cada linha da coluna_alvo
        df["Codigos_Extraidos"] = df[coluna_alvo].apply(extrair_codigos)

        # 7. SALVAR O NOVO ARQUIVO EXCEL
        # O DataFrame inteiro (com a nova coluna) é salvo em um novo arquivo
        # 'index=False' evita que o índice do pandas seja salvo como uma coluna no Excel
        df.to_excel(caminho_novo, index=False)

        print(f"Processo concluído com sucesso!")
        print(f"O novo arquivo foi salvo em: {caminho_novo}")

    else:
        print(f"Erro: O arquivo '{caminho_original}' não possui a 7ª coluna (Coluna G).")

except FileNotFoundError:
    print(f"Erro: Arquivo não encontrado. Verifique o caminho: {caminho_original}")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")