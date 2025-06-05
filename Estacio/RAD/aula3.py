
# AULA DE EXEÇÕES
#try:
#    numero =int(input("Digite um número inteiro: "))
#    print(f"Você digitou o número {numero}.")
#except ValueError:
#    print("Entrada inválida. Digite um número inteiro válido.")

# BIBLIOTECA RANDOM
#import random
#nome1 = str(input("Digite o primeiro nome:"))
#nome2 = str(input("Digite o segundo nome:"))
#nome3 = str(input("Digite o terceiro nome:"))
#nome4 = str(input("Digite o quarto nome:"))
#lista_nomes = [nome1, nome2, nome3, nome4]
#selecionado = random.choice(lista_nomes)
#print(f"O nome selecionado foi: {selecionado}")

#EXTRACAO DE UNIDADES

#def extrair_unidades(numero):
#    unidade = 0
#    dezena = 0
#    centena = 0
#    milhar = 0

    ##Verifica se o número é positivo
#    if numero >= 0:
        ## 1 % 10 = 1 porque?
        ## 1/10 é igual a zero pois 1 é menor que dez
        ## 0 (quociente da divisão) vezes 10 é igual a zero
        ##e 1 - 0 é igual a 1, portanto resta 1 de 1%10

        ##Extraindo a unidade
        # O % se chama modulo essa operação retorna o RESTO da divisão INTEIRA
#        unidade = numero % 10

        ##Eliminando a unidade do número original
        # O // faz a divisão do numero e retornar apenas a parte INTEIRA da divisão
#        numero //= 10

        ##Extraindo a dezena
#        dezena = numero % 10

        ##Eliminando a dezena do número original
#        numero //= 10

        ##Extraindo a centena
#        centena = numero % 10

        ##Eliminando a centena do número original
#        numero //=10

        ##O que sobrar é o milhar
#        milhar = numero

#        print(f"{milhar} milhar(res), {centena} centena(s), {dezena} dezena(s) e {unidade} unidade(s)")
#    else:
#        print("Por favor, insira um número inteiro positivo.")

#Solicitando o numero ao usuario
#numero = int(input("Digite um número inteiro positivo:"))
#extrair_unidades(numero)


# USANDO O COMANDO FIND

def analisar_frase(frase):
    frase = frase.lower()
    total_a = frase.count("a")
    primeira_posicao = frase.find("a")+1
    ultima_posicao = frase.rfind("a")+1
    print(f"Qtd de vezes que 'a' aparece na frase: {total_a}")
    print(f"Primeiro 'a': {primeira_posicao}")
    print(f"Ultimo 'a': {ultima_posicao}")

frase = str(input("Digite uma frase:"))
analisar_frase(frase)