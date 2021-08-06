# algoritmo para criar uma lista de tarefas simples(como lavar a roupa, fazer as compras e etc...)
# com a possibilidade de apagar e refazer tarefas

import os

sair = True
tarefas = []
tarefas_excluidas = []


def escolha(op):    # função para verificar se o input do usuário foi correto
    return op != 'add' and op != 'show' and op != 'undo' and op != 'redo' and op != 'exit'


def adicionar(lista):   # função para adicionar tarefas a lista
    lista.append(input('Digite a tarefa que quer adicionar: '))


def mostrar(lista):    # função para demonstrar as tarefas na lista
    for i in range(len(lista)):
        print(f'\tTarefa {i + 1}: {lista[i]}')
    input()


def excluir(lista, lista_excluidos):    # função para excluir tarefas da lista,
    # verificando primeiro se tem tarefas a serem excluídas
    if len(lista) == 0:
        print('Não há tarefas para excluir!')
    else:
        lista_excluidos.append(lista[len(lista) - 1])   # outra opção era criar uma variável temporária
        # e dar o pop ao mesmo tempo: temp = lista.pop()
        # lista_excluidos.append(temp)
        lista.pop()
        print('Tarefa excluída com sucesso.')


def refazer(lista, lista_excluidos):    # função para refazer tarefas apagadas da lista,
    # verificando primeiro se há tarefas a refazer
    if len(lista_excluidos) == 0:
        print('Não tem mais tarefas para refazer!')
    else:
        lista.append(lista_excluidos[len(lista) - 1])
        lista_excluidos.pop()
        print('Tarefa restaurada.')


while sair:   # parte principal do código para realizar as operações sobre a lista de tarefas
    os.system('cls')
    print('Que operação deseja realizar?')
    print('\tadd: Adicionar tarefas')
    print('\tshow: Ver a lista de tarefas')
    print('\tundo: Desfazer a última tarefa')
    print('\tredo: Refazer a última tarefa')
    print('\texit: Sair do programa')
    operacao = input('Opção: ')

    while escolha(operacao):
        operacao = input('Opção inválida! Digite novamente: ')

    if operacao == 'add':
        adicionar(tarefas)

    elif operacao == 'show':
        mostrar(tarefas)

    elif operacao == 'undo':
        excluir(tarefas, tarefas_excluidas)

    elif operacao == 'redo':
        refazer(tarefas, tarefas_excluidas)

    elif operacao == 'exit':
        sair = False
