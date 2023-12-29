#Esboço da ideia em portugol 

F: real
c: real

Escreva("Qual a temperatura?  ")
leia(F)
c <- (F - 32) /1.8

Escreva("No brasil seria:  ", c:4:1)
#c:4:1 formata o número





#Conversor de Fahrenheit para Celsius

f = float(input("Qual é a temperatura em Fahrenheit?  "))


c = (f - 32) / 1.8 

#Função round arredonda o número. Escolhi 1 casa decimal
a = round(c, 1)

print("A temperatura em graus Celsius é:", a)

