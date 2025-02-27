# PRIMEIRA AULA DE RAD 27/02/2025
import math

num1=float(input("Digite um numero: "))
num2=float(input("Digite o segundo numero: "))

ant1= num1-1
sus1= num1+1
dobro1=num1*2
triplo1=num1*3
quad1= math.sqrt(num1)
km=num1/1000
hec=num1/100
deca=num1/10
deci=num1*10
cem=num1*100
mili=num1*1000
dolar=num1/4.97
area=num1*num2
tinta=area/2

print("O numero digitado foi ",num1,".")
print("O antecessor desse numero é",ant1,".")
print("O sucessor desse numero é",sus1,"," )
print("O dobro desse numero é ",dobro1)
print("O triplo desse numero é ",triplo1)
print("A raiz quadrada desse numero é ",quad1)
print("O valor em quilometros é",km,"km")
print("O valor em hectometros é",hec,"hec")
print("O valor em decametros é",deca,"deca")
print("O valor em decimetros é",deci,"deci")
print("O valor em centimetros é",cem,"cem")
print("O valor em milimetros é",mili,"mili")
print(f'O valor em dolar é {dolar:.2f}')
print(f'A area da parede é {area}m2 e vai precisar de {tinta}L para pintar')