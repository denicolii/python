# Crie um programa que solicite ao usuário uma frase e conte quantas vogais (a, e, i, o, u) há na frase.

frase = str(input('Digite uma frase: '))
minusculo = frase.lower()
letraa = minusculo.count("a")
letrae = minusculo.count("e")
letrai = minusculo.count("i")
letrao = minusculo.count("o")
letrau = minusculo.count("u")

print('letra A: ',letraa )
print('letra E: ',letrae )
print('letra I: ',letrai )
print('letra O: ',letrao )
print('letra U: ',letrau )

