############################################

#def extrair_nomes(nome_completo):
#    partes=nome_completo.split();
#    primeiro_nome=partes[0];
#    segundo_nome=partes[-1];
#    print(f"Primeiro nome: {primeiro_nome}");
#    print(f"Segundo nome: {segundo_nome}");
#nome_digitado = input("Digite um nome completo: ");
#extrair_nomes(nome_digitado);

############################################

#distancia = float(input("Digite a distância da viagem(km): "))
#if distancia<=200:
#    valor_gasto=distancia*0.5
#else:
#    valor_gasto=distancia*0.45
#print(f"O valor da passagem é R${valor_gasto}")

############################################

import os

os.environ["REPLIT_DB_URL"] = "https://kv.replit.com/v0/eyJhbGciOiJIUzUxMiIsImlzcyI6ImNvbm1hbiIsImtpZCI6InByb2Q6MSIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJjb25tYW4iLCJleHAiOjE3NDMyMjYyNTAsImlhdCI6MTc0MzExNDY1MCwiZGF0YWJhc2VfaWQiOiJiOWUwNTAyNy0zOGVkLTQ4NjUtODllMS1jZGQyOGE3YzZmZWYifQ.llqH3HX_e2oGqJvcL1FQSLM0U__wDXUt8TVM4CVbKhN4aC43R_Jmi15YkLslmbZKHf-tFLwUnq5ByWQttcrvfg"

from replit import db

db["minha_lista"] = [10,20,30,40,50]

print(db["minha_lista"])
for item in db["minha_lista"]:
  print(item)

valor=db["minha_lista"][1]
print(f"Valor na segunda posição: {valor}")

print("Valores da lista original:")
for item in db["minha_lista"]:
  print(item)

db["minha_lista"].append(60)
db["minha_lista"].append(70)

print("\nLista atualizada:")
for item in db["minha_lista"]:
  print(item)

db["minha_lista"].pop()
print("\nLista após a remoção:")
for item in db["minha_lista"]:
  print(item)

db["minha_lista"][1] =25
valor_segundo_elemento=db["minha_lista"][1]
print(f"Valor do segundo elemento: {valor_segundo_elemento}")

print("\nLista atualizada:")
for item in db["minha_lista"]:
  print(item)

del db["minha_lista"][0]

print("\nLista atualizada:")
for item in db["minha_lista"]:
  print(item)

db.close()

produtos = [("Lapis", 1.75), 
            ("Borracha", 2.00),
            ("Caderno", 15.90),
            ("Estojo", 25.00),
            ("Transferidor", 4.20),
            ("Compasso", 9.99),
            ("Mochila", 120.32),
            ("Caneta", 22.30),
            ("Livro", 34.90),]

print("-"*40)
print(f"{'Lista de preços':^40}")
print("-"*40)

for produto, preco in produtos:
    print(f"{produto:.<30}R${preco:>7,.2f}")

print("-"*40)

def cadastro_unico ():
    valores_unicos = []
    while True:
        try:
            numero = int(
                input("Digite:")
            )
            if (numero<0):
                print("Digite:")
                cadastro_unico()
            if numero ==0:
                break
            if numero not in valores_unicos:
                valores_unicos.append(numero)
            else:
                print("Valor duplo")
        except ValueError:
            print("Digite um numero valido")

    valores_unicos.sort()

    if valores_unicos:
        print("\nValores digitados:")
    for valor in valores_unicos:
        print(valor)

cadastro_unico()