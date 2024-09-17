class ContaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo
        
    def get_saldo(self):
        return self.__saldo
    
    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de {valor} foi efetuado com sucesso!")
        else:
            print(f"Saldo insuficiente {self.__saldo - valor} para o saque!")
            
    def depositar(self, valor):
        self.__saldo += valor
        print(f"Deposito de {valor} foi efetuado com sucesso!")
        

conta = ContaBancaria("João", 1000)
print(conta.get_saldo())
conta.sacar(500)
print(conta.get_saldo())
conta.depositar(500)
print(conta.get_saldo())
conta.sacar(1200)
print(conta.get_saldo())
            