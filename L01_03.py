dias = int(input(' entre com a quantidade de dias: '))
horas = int(input(' entre com a quantidade de horas: '))
minutos = int(input(' entre com quantidade de minutos: '))
segundos = int(input(' entre com a quantidade de segundos '))
soma = segundos
dias = dias*86400
soma = soma + dias
horas = horas*3600
soma = soma + horas
minutos = minutos*60
soma = soma + minutos
print (f'A quantidade de dias em segundos he: {dias}')
print (f'A quantidade de horas em segundos he: {horas}')
print (f'A quantidade de minutos em segundo he: {minutos}')
print (f' O total de tudo em segundos he: {soma} ')
