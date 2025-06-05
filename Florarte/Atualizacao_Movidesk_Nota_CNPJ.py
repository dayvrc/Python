import requests
import pandas as pd

# --- CONFIGURAÇÕES ---
token = '45ab9045-e748-46fa-9818-9209246eed17'
ticket_id = 93701
arquivo_excel = r'D:\COD_CLIENTE.xlsx'

# --- LEITURA DA PLANILHA ---
df = pd.read_excel(arquivo_excel, header=None)
coluna_busca = df.iloc[:, 0].astype(str)  # Primeira coluna
coluna_retorno = df.iloc[:, 1].astype(str)  # Segunda coluna

# --- GET TICKET ---
url_get = f"https://api.movidesk.com/public/v1/tickets?token={token}&id={ticket_id}&$select=customFieldValues"
response_get = requests.get(url_get)

if response_get.status_code != 200:
    print("Erro ao buscar ticket:", response_get.status_code)
    print(response_get.text)
    exit()

ticket_data = response_get.json()
custom_fields = ticket_data.get("customFieldValues", [])

# --- PEGAR O VALOR DO CAMPO CPF/CNPJ ---
cpf_cnpj_valor = None
for campo in custom_fields:
    if campo.get("customFieldId") == 150500:
        cpf_cnpj_valor = campo.get("value")
        break

if not cpf_cnpj_valor:
    print("Campo CPF/CNPJ (150500) não encontrado ou vazio.")
    exit()

# --- BUSCAR CÓDIGO CLIENTE NA PLANILHA ---
if cpf_cnpj_valor in coluna_busca.values:
    index = coluna_busca[coluna_busca == cpf_cnpj_valor].index[0]
    codigo_cliente = coluna_retorno[index]
else:
    print("CPF/CNPJ não encontrado na planilha.")
    exit()

# --- MANTER OS CAMPOS EXISTENTES E ATUALIZAR APENAS O NECESSÁRIO ---
# Substituir ou adicionar o campo de código do cliente
campo_encontrado = False
for campo in custom_fields:
    if campo.get("customFieldId") == 153739:
        campo["value"] = codigo_cliente
        campo_encontrado = True
        break

if not campo_encontrado:
    custom_fields.append({
        "customFieldId": 153739,
        "customFieldRuleId": 75711,
        "line": 1,
        "value": codigo_cliente,
        "items": []
    })

# --- PATCH PARA ATUALIZAR O TICKET ---
url_patch = f"https://api.movidesk.com/public/v1/tickets?token={token}&id={ticket_id}"
payload = {
    # AQUI ELE ESTÁ FAZENDO UMA AÇÃO PUBLICA NO TICKET
    "actions": [
        {
            "type": 1,
           "description": "Atualização via API - Pegando CPF consultando em excel e trazendo o Cod do cliente.",
            "createdBy": {
                "id": "1616933282"
            }
        }
    ],
    "customFieldValues": custom_fields
}

headers = {
    "Content-Type": "application/json"
}

response_patch = requests.patch(url_patch, json=payload, headers=headers)

if response_patch.status_code == 200:
    print("Ticket atualizado com sucesso!")
else:
    print("Erro ao atualizar ticket:", response_patch.status_code)
    print(response_patch.text)
