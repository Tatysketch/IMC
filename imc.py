peso = float(input('Qual é seu peso?'))
altura = float(input('Qual é a sua altrua'))
imc = peso / (altura**2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5: 
    print('Voce está abaixo do peso ')
elif 18.5 <= imc < 25:
    print('Peso normal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
elif imc >= 40:
    print('Obesidade morbida')
    