# 12) Escreva um algoritmo que leia 20 valores inteiros e ao final exiba:
# A) a soma dos números positivos;
# B) a quantidade de valores negativos
def positivoNegativo ():
    soma = 0
    ctng = 0

    for i in range (20):
        num = int(input('{}º numero: '.format(i+1)))
    #A=Soma dos positivos
    if (num > 0):
        soma += num
    #B=Contando negativos
    elif(num < 0):
        ctng += 1
    return 'Positivos: {} \n Contar Negaivo: {} '.format(soma, ctng)