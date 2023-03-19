entrada_usuario = int(input('Você quer calcular o fatorial de qual número? '))
if entrada_usuario == 0:
    print('O fatorial de 0 é 1')
elif entrada_usuario < 0:
    print('Não é possível calcular o fatorial de um número negativo!')
else:
    fatorial = entrada_usuario
    for i in range(1, entrada_usuario):
        fatorial *= i
    print('O fatorial de {} é {}'.format(entrada_usuario, fatorial))
