class ContaBancaria:
    """
    Cria uma conta bancaria e permite fazer saques e depósitos
    """

    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo"
    
    def depositar(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if valor > self.saldo:
            print(f"Saque de R${valor:,.2f} negado. \nSALDO INSUFICIENTE")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:,.2f} autorizado.\nSaldo restante de R${self.saldo:,.2f}")

            
conta_1 = ContaBancaria(2907, "Gabriel", 5500)
conta_1.saque(5000)
print(conta_1)