class ContaBancaria:
    def __init__(self, saldo, titular):
        self.__saldo = saldo
        self.__titular = titular

    def depositar(self, valor):
        self.__saldo += valor
    
    def sacar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente!")
    
    def consulta(self):
        return self.__saldo
    
    def titularidade(self):
        return self.__titular


conta = ContaBancaria(1000000, "Joao")
print("Titutar: ", conta.titularidade())
print("Saldo atual: ", conta.consulta())

conta.depositar(1)
print("Novo Saldo atual: ", conta.consulta())

conta.sacar(1000000)
print("Novo Saldo atual: ", conta.consulta())
