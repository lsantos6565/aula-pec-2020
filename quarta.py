hora = int(input('Insira a hora atual: '))
minutos= int((input('Insira os minutos: ')))
segundos = int(input('Insira os segundos: '))

segundosTotais = (hora * 3600) + (minutos * 60) + (segundos)

print(f'Se passaram {segundosTotais} segundos desde a meia noite.')
