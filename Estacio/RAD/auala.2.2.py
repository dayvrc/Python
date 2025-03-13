texto = str(input("Digite um texto: "))

print(f"Contagem: {len(texto)}")

print(f"Minusculo: {texto.lower()}")

print(f"Maisculo: {texto.upper()}")

print(f"{texto.strip()}")

print(f"Separar: {texto.split()}")

partes = texto.strip().split
print(partes)