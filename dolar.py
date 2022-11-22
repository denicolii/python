dolar = float(input('Digite o valor em dólares que deseja converter: '))
cotacao =  float(input('Digite a cotação do dia: '))
conversao = cotacao*dolar
conversao = round((conversao), 2)

print ('O valor que você possui em reais é de: ', conversao)