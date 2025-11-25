class ContaBancaria:
    def __init__(self, numero, titular,saldo_inicial=0):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo_inicial
        self.__historico =[]
        self.__adicionar_transacao("Abertura", saldo_inicial)
    
    def __adicionar_transacao(self, tipo, valor):
        from datetime import datetime
        transacao = {
            "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
            "tipo": tipo,
            "valor": valor,
            "saldo": self.__saldo
        }
        self.__historico.append(transacao)

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            self.__adicionar_transacao("Depósito", valor)
            print(f"Depósito de R${valor:.2f}")
            return True
        else:
            print("Valor inválido")
            return False

    def sacar(self, valor):
        if valor == 0:
            print("Valor inválido")
            return False
        elif self.__saldo >= valor:
            self.__saldo -= valor
            self.__adicionar_transacao("Saque", -valor)
            print(f"Saque de R${valor:.2f}")
            return True
        else: 
            print("Saldo insuficiente.")
            return False
            
    def transferir(self, destino, valor):
        if self.sacar(valor):
            destino.depositar(valor)
            self.__adicionar_transacao(f"Transferência para conta {destino.numero}", -valor)
            destino.__adicionar_transacao(f"Transferência para conta {self.numero}", valor)
            print(f"Transferência de R${valor:.2f} realizada com sucesso.")
            return True
        return False

    def consultar(self):
        return self.__saldo
    
    def extrato(self):
        print(f"\n=== Extrato da Conta {self.__numero} ===")
        print(f"Titular: {self.__titular}")
        print(f"Saldo atual: R${self.__saldo:.2f}")
        print("\nHistórico de transações:")
        print("-" * 30)

        for transacao in self.__historico:
            valor_formatado = f"R${transacao['valor']:+.2f}"
            print(f"{transacao['data']} | {transacao['tipo']:20} | {valor_formatado:>10} | Saldo: R${transacao['saldo']:.2f}")

    @property
    def numero(self):
        return self.__numero
    
    @property
    def titularidade(self):
        return self.__titular

def main():
    conta1 = ContaBancaria("001", "João Silva", 1000.00)
    conta2 = ContaBancaria("002", "Maria Santos", 500.00)
    
    print("=== Situação Inicial ===")
    print(f"Conta {conta1.numero} - {conta1.titular}: R${conta1.consultar_saldo():.2f}")
    print(f"Conta {conta2.numero} - {conta2.titular}: R${conta2.consultar_saldo():.2f}")
    print()
    
    conta1.depositar(300.00)
    conta1.sacar(150.00)
    conta1.transferir(conta2, 200.00)
    
    print("\n=== Situação Final ===")
    print(f"Conta {conta1.numero}: R${conta1.consultar_saldo():.2f}")
    print(f"Conta {conta2.numero}: R${conta2.consultar_saldo():.2f}")
    print()
    
    conta1.extrato()
    print()
    conta2.extrato()

if __name__ == '__main__':
    main()
