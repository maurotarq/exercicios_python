def entrada():  # função para receber o input do usuário
    cnpj = input('Digite um cnpj: ')
    return cnpj


def limpar_entrada(cnpj):   # função para formatar o input, e deixar o cnpj como uma string contendo apenas números
    return cnpj.replace('.', '').replace('-', '').replace('/', '')


def sequencia(cnpj):    # função para verificar se o cnpj inserido é uma sequência(no caso de cnpjs apenas 00... valida)
    seq = cnpj[0] * len(cnpj)

    if seq == cnpj:
        return True
    else:
        return False


def primeiro_digito(novo_cnpj):    # função que calcula o penúltimo digito do cnpj
    mult = 5
    soma = 0

    for i in range(12):
        soma += int(novo_cnpj[i]) * mult

        mult -= 1
        if mult < 2:
            mult = 9

    d = 11 - (soma % 11)
    d = d if d <= 9 else 0

    novo_cnpj += str(d)
    return novo_cnpj


def segundo_digito(novo_cnpj):  # função que calcula o último dígito do cnpj,
    # talvez fosse melhor ter programado uma função para calcular os dois digitos
    mult = 6
    soma = 0

    for i in range(13):
        soma += int(novo_cnpj[i]) * mult
        mult -= 1

        if mult < 2:
            mult = 9

    d = 11 - (soma % 11)
    d = d if d <= 9 else 0

    novo_cnpj += str(d)
    return novo_cnpj


def valida():   # função principal que chama todas as outras para realizar a verificação do cnpj
    cnpj = limpar_entrada(entrada())
    novo_cnpj = cnpj[:-2]
    try:
        novo_cnpj = segundo_digito(primeiro_digito(novo_cnpj))
    except:
        return False, cnpj

    if not novo_cnpj == cnpj or sequencia(cnpj):
        return False, formata(cnpj)
    else:
        return True, formata(cnpj)


def formata(cnpj):  # função que formata a saída
    formatado = f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}'
    return formatado