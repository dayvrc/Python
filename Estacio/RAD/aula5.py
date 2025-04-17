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