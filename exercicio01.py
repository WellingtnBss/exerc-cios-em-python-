
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



    

    



