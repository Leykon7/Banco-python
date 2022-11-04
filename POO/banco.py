from contas import Conta, ContaPoupanca

class banco ():
    def __init__(self):
        self.contas = [ Conta(0, "Gerente", 5555, 0),
                        Conta(1,"Joao",1234,300),
                        ContaPoupanca(2,"Jose",4567,saldoi=800),
                        Conta(3, "Maria", 7890, 1000),
                        ContaPoupanca(4, "Madalena", 8956, saldoi = 2000) ]



    def BuscaConta (self, numC):
        for contaq in self.contas:
            if contaq.numero == numC:
                return contaq
        print("Conta Invalida!")
        return None
        


    def atendimento(self):
        atendimento = True
        while atendimento:
            print("\n\nBem vindo ao sistema de atendimento do banco\n")
            op = int(input("\nVocê é cliente ou Gerente?(0 - Cliente | 1 - Gerente): "))
            if op == 0:
                self.atendeCliente()
            elif op == 1:
                self.atendeGerente()
            else:
                print("invalido!")

            op = int(input("\n\nDeseja deseja continuar?(0 - Não | 1 - Sim): "))
            if op == 0:
                atendimento = False



    def atendeCliente(self):
        atendimento = True
        
        numC = int(input("Digite o numero de sua conta: "))
        ContaCliente = self.BuscaConta(numC)
        
        if ContaCliente == None:
            atendimento = False
        else:
            senhain = int(input("Digite sua senha: "))
            while atendimento:
                if ContaCliente.ValidaSenha(senhain):
                    print(f"\nBem vindo {ContaCliente.titular}!")
                    op = int(input("\nQual operacao deseja fazer?(1 - Saque, 2 - Deposito, 3 - Ver Saldo, 4 - Transferencia, 5 - Sair): "))
                    
                    if op == 1:
                        valor = float(input("Digite o valor: "))
                        if ContaCliente.saque(senhain, valor):
                            print(f"Saque no valor de R$ {valor} realizado com sucesso\n")
                        else:
                            pass

                    elif op == 2:
                        valor = float(input("Digite o valor: "))
                        if ContaCliente.deposito(valor):
                            print(f"Depósito no valor de R$ {valor} realizado com sucesso\n")
                        else:
                            pass

                    elif op == 3:
                        print("Seu saldo é de R$ ", ContaCliente.getSaldo(senhain))
                    elif op == 4:
                        ContaCliente2 = int(input("Digite o numero da conta para qual deseja transferir: "))
                        ContaCliente2 = self.BuscaConta(ContaCliente2)
                        valor = float(input("Digite o valor: "))
                        if ContaCliente.transferencia(senhain, valor, ContaCliente2):
                            print(f"Transferência de {valor} realizada com sucesso para a conta de {ContaCliente2.titular} realizada com sucesso\n")
                    else:
                        atendimento = False
                        pass
                else:
                    print("Senha incorreta")
                    atendimento = False
                    pass



    def atendeGerente(self):
        ContaCliente = self.BuscaConta(0)
        senhain = int(input("Digite a senha: "))
        atendimento = True
        if ContaCliente.ValidaSenha(senhain):
                while atendimento:
                    op = int(input("\nQual operacao deseja fazer?(1 - Criar conta | 2 - Deletar conta | 3 - Sair): "))
                    if op == 1:
                        nome = input("\nDigite o nome: ")
                        senha = int(input("Digite sua senha: "))
                        saldo = int(input("Digite o saldo inicial: "))
                        op = int(input("A conta é poupança ou corrente?(1 - Poupança | 2 - Corrente): "))

                        if op == 1:
                            taxa = float(input("Digite a taxa: "))
                            self.contas.append(ContaPoupanca(len(self.contas), nome, senha, taxa, saldo))
                            print(f"Conta {len(self.contas)-1} de {nome} criada com sucesso")
                        elif op == 2:
                            self.contas.append(Conta(len(self.contas), nome, senha, saldo))
                            print(f"Conta {len(self.contas)-1}, de {nome} criada com sucesso")
                        else:
                            pass

                    elif op == 2:
                        numC = int(input("Digite o numero da conta: "))
                        self.contas.pop(numC)
                        #Criar método que descobre o verdadeiro índice da conta na lista contas
                    else:
                        atendimento = False
                        pass
        else:
            print("Senha incorreta")