import re
import pandas as pd

# Caminho do arquivo Excel
arquivo = r"C:\Users\drdc\Downloads\Estúdio_-_Solicitações-2025-08-25-15h-03m-15s.xlsx"

# Regex para capturar diferentes formatos de códigos
padrao = re.compile(r"\b\d{6,8}F?\b|\b\d{5}-\d{3}\b")

# Ler a planilha inteira
df = pd.read_excel(arquivo)

# Garantir que a coluna G existe (índice 6 → 7ª coluna)
coluna_g = df.columns[6]

# Função para extrair códigos
def extrair_codigos(texto):
    if pd.isna(texto):
        return ""
    codigos = padrao.findall(str(texto))
    return ",".join(codigos)

# Criar a nova coluna
df["Codigos_Extraidos"] = df[coluna_g].apply(extrair_codigos)

# Salvar no mesmo arquivo (sobrescrevendo)
with pd.ExcelWriter(arquivo, engine="openpyxl", mode="w") as writer:
    df.to_excel(writer, index=False)
