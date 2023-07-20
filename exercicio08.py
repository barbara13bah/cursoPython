# 8) Escrever um algoritmo que leia 10 números inteiros e, ao final, apresente a soma de todos os números lidos
def numeros ():
    soma = 0
    for i in range(1, 11, 1):
        num = int(input('{}º numero: '.format(i)))
        soma += num
    return 'O total de todos é: {}'.format(soma)


