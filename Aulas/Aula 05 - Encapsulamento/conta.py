
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print('contruindo objeto...')
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular}')

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):

        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print('Não é possível realizar o saque, valor passou do limite')

    def transfere(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    def __pode_sacar(self, valor):

        if valor <= self.__saldo:
            return True
        else:
            return False

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor):
        self.__limite = valor

    @staticmethod
    def codigo_banco():
        cod = {
            'BB': '001',
            'Caixa': '104',
            'Bradesco': '237'
        }
        return cod
