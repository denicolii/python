altura = float(input('Digite a sua altura em metros: '))
peso = float (input('Digite seu peso: '))
resposta = peso / (altura*altura)
print ('Seu IMC é de: ', resposta)

if resposta <= 16.9 : 
    print ('você está muito abaixo do seu peso ideal, procure um nutricionista!')

elif  resposta == 17 or resposta <= 18.4 :
    print ('você está  abaixo do seu peso ideal, procure um nutricionista!')

elif resposta == 18.5 or resposta <= 24.9 : 
    print ('Parabéns, você está no peso ideal')

elif  resposta == 25  or resposta <= 29.9 : 
    print ('Obesidade grau 1, procure um médico!')

elif resposta == 35 or resposta <= 40 :
    print ('Obesidade grau 2, procure um médico!')

elif ('resposta >= 40.1') :
    print ('Obesidade grau III, procure um médico urgentemente!')