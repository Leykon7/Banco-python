from contas import Conta, ContaPoupanca
class banco ():
    def __init__(self):
        self.contas = [Conta(0, "Gerente", 5555, 0),
                  Conta(1,"Joao",1234,300),
                  ContaPoupanca(2,"Jose",4567,saldoi=800),
                  Conta(3, "Maria", 7890, 1000),
                  ContaPoupanca(4, "Madalena", 8956, saldoi = 2000)]
        self.NContas = 5
    def BuscaConta (self,numC):
        for Nconta in self.contas:
            if Nconta.numero == numC:
                return Nconta
        print("Conta Invalida!")
        return None
        
    def atendeCliente(self):
            numC = int(input("Digite o numero de sua conta: "))
            ContaCliente = self.BuscaConta(numC)
            senhain = input("Digite sua senha: ")

            if ContaCliente.ValidaSenha(senhain):
                op = int(input("\n\nQual operacao deseja fazer? (1 - Saque, 2 - Deposito, 3 - Ver Saldo, 4 - Transferencia, 5 - Sair): "))
                if op == 1:
                    valor = float(input("Digite o valor: "))
                    ContaCliente.saque(senhain, valor)

                elif op == 2:
                    valor = float(input("Digite o valor: "))
                    ContaCliente.deposito(valor)
                elif op == 3:
                    ContaCliente.getSaldo(senhain)
                elif op == 4:
                    numC = int(input("Digite o numero da conta para qual deseja transferir: "))
                    numC = self.BuscaConta(numC)
                    valor = float(input("Digite o valor: "))
                    ContaCliente.transferencia(senhain, valor, numC)
                else:
                    pass
            else:
                print("Senha incorreta")
            

    def atendeGerente(self):
        numC = int(input("Digite o numero de sua conta: "))
        ContaCliente = self.BuscaConta(numC)
        senhain = input("Digite sua senha: ")

        if ContaCliente.ValidaSenha(senhain):
                op = int(input("\n\nQual operacao deseja fazer? (1 - Criar conta | 2 - Deletar conta | 3 - Sair): "))
                if op == 1:
                    nome = input("Digite o nome: ")
                    senha = int(input("Digite sua senha: "))
                    saldo = int(input("Digite o saldo inicial: "))
                    op = int(input("A conta é poupança ou corrente: (1 - Poupança | 2 - Corrente) "))

                    if op == 1:
                        taxa = float(input("Digite a taxa: "))
                        self.contas.append(ContaPoupanca(self.NContas, nome, senha, taxa, saldo))
                        self.NContas+=1
                    elif op == 2:
                        self.contas.append(Conta(self.NContas, nome, senha, saldo))
                        self.NContas+=1
                elif op == 2:
                    numC = int(input("Digite o numeo da conta: "))
                    self.contas.pop(numC)
                else:
                    pass
        else:
            print("Senha incorreta")


    def atendimento(self):
        atendimento = True
        while atendimento:
            print("Bem vindo ao sistema de atendimento do banco\n")
            op = int(input("Você é cliente ou Gerente?: (0 - Cliente | 1 - Gerente"))
            if op == 0:
                self.atendeCliente()
            elif op == 1:
                self.atendeGerente()
            else:
                print("invalido!")

            op = int(input("Deseja fazer mais operações?: (0 - Não | 1 - Sim"))
            if op == 0:
                atendimento = False
            else:
                atendimento = True