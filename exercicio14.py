# 14) Escreva um programa que leia um valor correspondente ao número de jogadores de um time de vôlei. O programa deverá ler uma altura para cada um dos jogadores e, ao final, informar a altura média do time
from  exercicio05 import coletarPositivo

def mediaVolei ():
    qtd = int(input('Informe a quantidade de pessoas no time: '))
    soma = 0
    for i in range (qtd):
        altura = coletarPositivo()
        soma += altura
    return 'A altura media do time é {}'.format(soma/qtd)