
#Conversor de Fahrenheit para Celsius

f = float(input("Qual é a temperatura em Fahrenheit?  "))


c = (f - 32) / 1.8 

#Função round arredonda o número. Escolhi 1 casa decimal
a = round(c, 1)

print("A temperatura em graus Celsius é:", a)

