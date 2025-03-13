import math

valor1 = float(input("Digite o valor do cateto oposto: "))
valor2 = float(input("Digite o valor do cateto adjacente: "))

valor3 = math.hypot(valor1,valor2)

print(f"A hipotenusa é: {valor3:.2f}")

print(math.isqrt(5))