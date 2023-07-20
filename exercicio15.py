#15) Em um concurso de miss, os jurados precisam digitar o nome das 16 candidatas e suas respectivas notas (0 a 10). Crie um programa que leia estas informações e que, ao final do programa, apresente apenas o nome e a nota da vencedora
def validNota():
    nota = float(input('Informe a nota: '))
    while ((nota < 0) or (nota > 10)):
        print('Erro, a nota varia de 0 a 10!')
        nota = float(input('Informe a nota: '))
    return nota


def miss ():
    ganhadora = ''
    notaFinal = 0
    for i in range(1, 17):
        nome = input('Informe o nome da {} ª candidata'.format(i))
        nota = validNota()
    if (nota > notaFinal):
            notaFinal = nota
            notaFinal = nome
    return 'Ganhadora: {} \n Nota: {}'.format(ganhadora, notaFinal)
