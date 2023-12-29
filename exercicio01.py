#Esboço em portugol

algoritmo "triangulos"
var 

   l1, l2, l3: Real
   EQ, ES, TRI: logico

inicio

       Escreva("Digite o primeiro lado: ")
       Leia(l1)
       Escreva("Digite o segundo lado")
       Leia(l2)
       Escreva("Digite o teerceiro lado: ")
       leia(l3)
       TRI <- (l1 < l2 + l3) e (l2 < l1 + l3) e (l3 < l1 + l2)
       EQ <- (L1 = L2) e (l2 = l3) 
       ES <- (L1 <> L2) e (l2 <> l3) e (l1 <> l3) 
       Escreval ("pode formar um TRIANGULO?  ", TRI)
       Escreval ("o triângulo é equilatero?   ", EQ)
       Escreval ("o triângulo é escaleno?     ", ES)

filalgoritmo





#O código verifica se os números inseridos pelo usuário podem formar triângulos.

l1 = int(input("Digite o primeiro lado: "))

l2 = int(input("Digite o segundo lado: "))

l3 = int(input("Digite o terceiro lado: "))


if l1 == l2 and l2 == l3: 
    print("Pode formar um triângulo equilatero")

elif l1 != l2 and l2 != l3 and l3 != l1:
    print("Pode formar um triângulo escaleno")

elif l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print("Pode formar um triângulo")



    

    



