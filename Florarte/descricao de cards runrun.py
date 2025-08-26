import requests
import pandas as pd
import re
import time
from pathlib import Path

# ========================================
# CONFIGURAÇÕES DO USUÁRIO
# ========================================

API_TOKEN = "SEU_TOKEN_AQUI"
WORKSPACE = "SEU_WORKSPACE_AQUI"
BOARD_ID = "SEU_BOARD_ID_AQUI"

# IDs de cards fechados que você quer coletar manualmente
CARDS_FECHADOS = [123456, 789012, 345678]  

# Caminho da planilha de SKUs
BASE_SKU_PATH = Path(r"C:\Users\drdc\OneDrive - D&A Decoração E Ambientação\BASE_Lista de Produtos.xlsx")

# Nome da aba final no Excel
OUTPUT_EXCEL = "resultado_cards.xlsx"
OUTPUT_SHEET = "base_runrunit_estudio"

# ========================================
# FUNÇÕES AUXILIARES
# ========================================

def get_cards_ativos():
    """Busca apenas IDs dos cards ativos criados em 2025"""
    url = f"https://{WORKSPACE}.runrun.it/api/v1.0/cards"
    params = {
        "board_id": BOARD_ID,
        "q": "status:open created:>=2025-01-01",
        "page_size": 100
    }
    headers = {"Authorization": f"Bearer {API_TOKEN}"}

    ids = []
    page = 1
    while True:
        params["page"] = page
        r = requests.get(url, headers=headers, params=params)
        if r.status_code != 200:
            print("Erro:", r.text)
            break
        data = r.json()
        if not data:
            break
        ids.extend([c["id"] for c in data])
        page += 1
        time.sleep(0.6)  # evitar limite de requisições
    return ids

def get_descricao(card_id):
    """Busca a descrição de um card"""
    url = f"https://{WORKSPACE}.runrun.it/api/v1.0/cards/{card_id}/description"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        return r.json().get("description", "")
    return ""

def extrair_skus(texto):
    """Extrai SKUs via regex (6 ou 8 dígitos, 8 dígitos + F, ou formato 12345-678)"""
    padroes = [
        r"\b\d{6}\b",            # 6 dígitos
        r"\b\d{8}\b",            # 8 dígitos
        r"\b\d{8}F\b",           # 8 dígitos + F
        r"\b\d{5}-\d{3}\b"       # formato com hífen (ex: 98849-001)
    ]
    skus = []
    for padrao in padroes:
        encontrados = re.findall(padrao, texto)
        skus.extend(encontrados)
    return list(set(skus))  # remove duplicados

# ========================================
# PIPELINE PRINCIPAL
# ========================================

def main():
    # 1. Buscar IDs de cards ativos
    ids_ativos = get_cards_ativos()

    # 2. Juntar com IDs de cards fechados definidos manualmente
    ids_total = ids_ativos + CARDS_FECHADOS

    registros = []
    for card_id in ids_total:
        descricao = get_descricao(card_id)
        skus = extrair_skus(descricao)
        if skus:
            for sku in skus:
                registros.append({"ID": card_id, "SKU": sku})
        else:
            registros.append({"ID": card_id, "SKU": None})
        time.sleep(0.6)

    df_cards = pd.DataFrame(registros)

    # 3. Carregar planilha de SKUs
    df_skus = pd.read_excel(BASE_SKU_PATH, sheet_name="Planilha1")
    df_skus = df_skus.rename(columns={"Cod_Produto": "SKU"})
    df_skus["SKU"] = df_skus["SKU"].astype(str).str.strip()

    # 4. Juntar (tipo PROCv)
    df_final = df_cards.merge(df_skus, on="SKU", how="left")

    # 5. Exportar para Excel
    with pd.ExcelWriter(OUTPUT_EXCEL, engine="openpyxl") as writer:
        df_final.to_excel(writer, sheet_name=OUTPUT_SHEET, index=False)

    print(f"✅ Arquivo gerado: {OUTPUT_EXCEL}")

# ========================================
if __name__ == "__main__":
    main()
