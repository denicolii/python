print("Calcular média de baixar de asfalto")
num1 = int(input("Quantos serviços a primeira equipe fez?:" ))
num2 = int(input("Quantos serviços a segunda equipe fez?:" ))
num3 = int(input("Quantos serviços a terceira equipe fez?:" ))
dias = int(input("Qauntos dias foram trabalhados?"))

soma = num1+num2+num3
media = (soma / 3)


print ("A média de serviços baixados durante ", dias, "foi de: ", round(media) )