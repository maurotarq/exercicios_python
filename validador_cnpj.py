from cnpj_modulos.modulos import valida

if __name__ == '__main__':
    val, num = valida()    # função mestre que chama várias outras funções
    if val:
        print(f'O CNPJ {num} é válido!')
    else:
        print(f'O CNPJ {num} é inválido!')