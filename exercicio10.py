# 10) Escreva um algoritmo que calcule a média dos números digitados pelo usuário, se eles forem pares. Termine a leitura se o usuário digitar zero (0)
def media():
    soma = 0
    num = 1
    i = 0
    while num != 0:
        num = int(input('Valor: '))
        if (num % 2 == 0):
            soma += num
            i += 1
            print('A media é: {}'.format(soma))
