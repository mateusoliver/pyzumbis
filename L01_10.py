cigaros = int(input('Qual a quantidade de cigarros fumados por dia: '))
anos = int(input('Quantos anos j´a fumou: '))
dianos = anos*365
totalcigaros = dianos*cigaros
tempo = totalcigaros*10
dias = tempo/1440

print (f'Voce perdeu {dias} dias de vida.')
