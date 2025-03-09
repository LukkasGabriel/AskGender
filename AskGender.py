sexo = str(input('Qual seu sexo? [M/F] ')).upper()

while sexo not in ['F', 'M']:
    print('Valor incorreto, tente novamente')
    sexo = str(input('Qual seu sexo? [M/F] ')).upper()


if sexo == 'M':
    print('Seja bem-vindo')
else:
    print('Seja bem-vinda')

