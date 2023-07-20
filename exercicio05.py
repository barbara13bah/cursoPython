# 5) Construa um programa que exiba a tabuada de 1 até N
def tabuada (num, n):
        for i in range (1, n+1):
            print('{} * {} = {}'.format(num, i, num * i))
def coletarPositivo ():
    num = float(input('Informe um numero: '))
    while (num <= 0):
        print('Erro, o numero precisa ser positivo!')
        num = int(input('Informe um numero: '))
    return num


