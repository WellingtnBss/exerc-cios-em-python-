#Esboço em portugol


m, a, imc:real


Escreva("massa (kg): ")
leia(m)
Escreva("altura (m): ")
leia(a)

imc <- m / (a ^ 2) 
Escreval("imc: ", imc:5:2)

Se (imc < 17) entao
   Escreval ("muito abaixo do peso")
senao
     Se (imc >= 17) e (imc < 18.5) entao
         Escreval ("Abaixo do peso")
     senao
          Se (imc >= 18.5) e (imc < 25) entao 
             Escreval ("Peso ideal") 
           senao
                 se (imc >= 25) e (imc < 30) entao
                    Escreval ("Sobrepeso")
                  senao
                       Se (imc >= 30) e (imc < 35) entao
                          Escreval("Obesidade")
                       senao
                            Se (imc >= 35) e (imc < 40) entao
                               Escreval("Obesidade severa")
                            senao
                                 Escreval("Obesidade morbida")




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










