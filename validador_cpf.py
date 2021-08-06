# algoritmo para verificar se um cpf inserido é válido

cpf = input('Digite um CPF(apenas números): ')
sequencia = cpf == str(cpf[0]) * len(cpf)

while not cpf.isnumeric() or len(cpf) != 11 or sequencia:
    if not cpf.isnumeric():
        print('Digite apenas números, sem pontos ou letras.')
    elif len(cpf) != 11:
        print('CPFs tem apenas 11 digitos!')
    else:
        print('CPFs não podem ser sequências de números.')
    cpf = input('Digite novamente: ')
    sequencia = cpf == str(cpf[0]) * len(cpf)

soma = 0
for dig, mult in enumerate(range(10, 1, -1)):
    soma += int(cpf[dig]) * mult

if 11 - (soma % 11) > 9:
    digito10 = 0
else:
    digito10 = 11 - (soma % 11)

soma = 0
for dig, mult in enumerate(range(11, 1, -1)):
    soma += int(cpf[dig]) * mult

if 11 - (soma % 11) > 9:
    digito11 = 0
else:
    digito11 = 11 - (soma % 11)

if digito10 == int(cpf[9]) and digito11 == int(cpf[10]):
    print('O CPF inserido é válido.')
else:
    print('CPF inserido inválido.')



