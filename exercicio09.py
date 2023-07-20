
# 9) Faça o mesmo que antes, porém, ao invés de ler 10 números, o programa deverá ler e somar números até que o valor digitado seja zero ( 0 )

def valores ():
    soma = 0
    num = 1
    i = 0
    while num != 0:
            num = int(input('{}º valor: '.format(i+1)))
            i += 1
            soma += num
    print('O total de todos é: {}'.format(soma))




