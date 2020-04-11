salario = float(input('entre com seu salario: '))
porcento = int(input('Entre com a porcentagem do aumento. Ex: 5, 16, 30. : '))
aumento = salario*porcento/100
salario = salario + aumento
print (f'seu salario final com o aumento he de: {salario}')
print (f'Voce teve um aumento de : {aumento}')
