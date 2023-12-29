
#Calcular o IMC

m = float(input("Qual a sua massa corporal: "))

at = float(input("Qual a sua altura: "))

imc = m /  (at ** 2)

a = round(imc, 1)

print("Seu imc é", a)

if imc < 17: 
    print("Muito abaixo do peso")

elif imc >= 17 and imc < 18.5:
    print("Abaixo do penso")

elif imc >= 18.5 and imc < 25:
    print("Peso ideal")

elif imc >= 25 and imc < 30:
    print("Sobrepeso")

elif imc >= 30 and imc < 35:
    print("Obesidade")

elif imc >= 35 and imc < 40:
    print("Obesidade severa")

else:
    print("obsidade mórbida")










