# Vetor Global = Todas as funções podem visualizar / usar esse vetor
notas = []
def preencherVetor (fim):
    for i in range (fim):
        num = int(input('Informe a {}ª nota: '.format(i+1)))
        #Add notas no vetor:
        notas.append(num)
def consultarVetor (fim):
    for i in range (fim):
        print(' {}ª posição: {}'.format(i+1,notas[i]))

#Excluir dado do vetor:
def apagarPosicao(posicao):
    if (len(notas) < posicao):
        print('Impossivel remover, pois o tamanho é menor que a posição')
    else:
        del (notas[posicao])
        print('Removido com sucesso')