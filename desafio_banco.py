from abc import ABC, abstractmethod


class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self._conta = []

    @property
    def conta(self):
        return self._conta

    def adicionar_conta(self, conta):
        if conta in self._conta:
            print('Essa conta já foi inserida')
            return

        self._conta.append(conta)
        print('Cliente recebeu conta com sucesso.')


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Saldo precisa ser um valor numérico')

        self._saldo = valor

    def deposito(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Deposito precisa ser um valor numérico')

        self._saldo += valor

    def informacoes(self):
        print(f'Agência: {self.agencia}', end=' ')
        print(f'Conta: {self.conta}', end=' ')
        print(f'Saldo: {self.saldo}')

    @abstractmethod
    def sacar(self, valor):
        pass


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    def sacar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Saque deve ser um valor numérico')

        if self.saldo + self.limite < valor:
            print('Saldo insuficiente.')
            return

        self.saldo -= valor


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Saque deve ser um valor numérico')

        if self.saldo < valor:
            print('Saldo insuficiente.')

        self.saldo -= valor


class Banco:
    def __init__(self, agencias):
        self._clientes = []
        self._contas = []
        self._agencias = agencias

    def autenticacao_agencia(self, agencia):
        if agencia in self._agencias:
            print('Agencia valida')
            return True

        return False

    def autenticacao_cliente(self, cliente):
        if cliente in self._clientes:
            print('Cliente valido')
            return True

        return False

    def autenticacao_conta(self, conta):
        if conta in self._contas:
            print('Conta valida')
            return True

        return False

    def autenticacao(self, agencia, cliente, conta):
        if self.autenticacao_agencia(agencia) and self.autenticacao_conta(conta):
            if self.autenticacao_cliente(cliente):
                if conta in cliente.conta:
                    return True

        return False

    def adicionar_cliente(self, cliente):
        if cliente in self._clientes:
            print('Esse cliente já foi inserido.')
            return

        self._clientes.append(cliente)
        print('Cliente adicionado com sucesso.')

    def adicionar_contas(self, conta):
        if conta in self._contas:
            print('Essa conta já foi inserida.')
            return
        if self.autenticacao_agencia(conta.agencia):
            self._contas.append(conta)
            print('Conta adicionada com sucesso')
            return

        print('Agência da conta inválida.')

    def saque(self, cliente, conta, valor):
        if self.autenticacao(conta.agencia, cliente, conta):
            conta.sacar(valor)
            conta.informacoes()
            return

        print('Impossível sacar.')


if __name__ == '__main__':
    pessoa = Cliente('Abacate', 32)
    conta_corrente = ContaCorrente(agencia=1111, conta=21000, saldo=1000, limite=500)
    conta_poupanca = ContaPoupanca(agencia=1111, conta=22000, saldo=1000)
    banco = Banco([1111, 2222])

    pessoa.adicionar_conta(conta_corrente)
    pessoa.adicionar_conta(conta_poupanca)

    banco.adicionar_contas(conta_corrente)
    banco.adicionar_contas(conta_poupanca)

    banco.adicionar_cliente(pessoa)

    banco.saque(pessoa, conta_corrente, 1000)
    banco.saque(pessoa, conta_poupanca, 500)
