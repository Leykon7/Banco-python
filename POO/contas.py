class Conta():
    """
    Classe Conta
    """
    _saldo = 0.0
    def __init__(self, numero, titular, senha,saldoi=0.0):
        """
        Construtor da classe Conta
        :param numero: número da conta
        :param titular: nome o titular da conta
        :param senha: senha da conta
        :param saldoi: saldo inicial da conta (padrão = 0.0)
        """
        self.numero = numero
        self.titular = titular
        self.__senha = senha
        self._saldo = saldoi
    
    def getSaldo(self, senha):
        """
        Método para obtenção do saldo mediante validação da senha passada como argumento
        :param senha: senha da conta
        :return: saldo da conta
        """
        if self.__senha == senha:
            return self._saldo

    def ValidaSenha(self, senhain):
        if senhain == self.__senha:
            return True
        else:
            return False


    def setSaldo(self, valor):
        """
        Método para configuração do saldo
        :param valor: valor desejado para o saldo
        """
        self._saldo = valor

    def setSenha(self, novaSenha):
        """
        Método para configuração de uma nova senha na conta
        :param novaSenha: nova senha desejada
        """
        self.__senha = novaSenha

    def saque(self, senha, valor):
        """
        Método para realização de um saque
        :param senha: senha da conta
        :param valor: valor do saque
        """
        if senha == self.__senha:
            if self._saldo >= valor:
                self._saldo -= valor
                return True
            else:
                print("Saldo insuficiente")
        else:
            print("Senha inválida")
        return False
    
    def deposito(self, valor):
        """
        Método para realização de um depósito
        :param valor: valor do deposito desejado
        """
        if valor > 0:
            self._saldo += valor
            return True
        else:
            print("Valor inválido")
            return False

    def exibeDados(self, senha):
        """
        Método para exibição das informações da conta
        :param senha: senha da conta
        """
        if self.__senha == senha:
            print("Número: ", self.numero)
            print("Titular: ", self.titular)
            print("Saldo: R$ ", self._saldo)
        else:
            print("Senha inválida")
    
    def transferencia(self, senha, valor, ContaCliente2):
        if self.saque(senha, valor):
            ContaCliente2.deposito(valor)
            return True
        else:
            print("A transferência falhou")
            return False


class ContaPoupanca(Conta):#Cria uma classe derivada da classe conta,mantendo todas as funções já definidas em Conta
    """
    Classe Conta Poupança
    """
    def __init__(self, numero, titular, senha, taxa = 0.002, saldoi=0.0):
        """
        Construtor da classe Conta
        :param numero: número da conta
        :param titular: nome o titular da conta
        :param senha: senha da conta
        :param taxa: taxa de rendimento mensal
        :param saldoi: saldo inicial da conta (padrão = 0.0)
        """
        super().__init__(numero,titular,senha,saldoi)#super() é utilizado para se referir a uma função da classe na qual essa é derivada, no caso o construtor da classe Conta
        self.__taxa = taxa
    
    def simulaRendimento(self, nmeses):
        """
        Método para simulação do rendimento do saldo em um determinado número de meses
        :param nmeses: número de meses que serão utilizados na simulação
        """
        if nmeses>0:
            saldo_final = self._saldo*pow((1+self.__taxa),nmeses)
            print(f"Saldo após {nmeses} meses : R$ {saldo_final:.2f}")
        else:
            print("Número de meses deve ser maior que zero")
