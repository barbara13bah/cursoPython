#16. Escreva um algoritmo para ler o número total de eleitores de um  nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao total de eleitores
def coletarPositivoInt():
    num = int(input())
    while (num <= 0):
        print('Erro! O valor é positivo!')
        num = int(input('Informe um numero: '))
    return num
def transformarPercent (num, total):
    percentual = (num/ total) * 100
    return percentual


def eleicao():
    print('Informe o total de votos brancos: ')
    branco = coletarPositivoInt()
    print('Informe o total de votos nulos: ')
    nulo = coletarPositivoInt()
    print('Informe o total de votos validos: ')
    valido = coletarPositivoInt()
    print('Informe o total de votos eleitores: ')
    total = coletarPositivoInt()
    if ((branco+nulo+valido) == total):
        pbranco = transformarPercent(branco,total)
        pnulo = transformarPercent(nulo, total)
        pvalido = transformarPercent(valido, total)
        return 'Votos brancos: {}% \n Votos nulos: {}% \n Votos validos: {}%'.format(pbranco,pnulo,pvalido)
    else:
        return 'nº brancos, validos e nulos é diferente do total de eleitores, tente novamente.'