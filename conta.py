class Conta:
    def __init__ (self, numero, titular, saldo, limite):
        # print("construindo objeto...{}".format(self))
        self.__numero  = numero
        self.__titular = titular
        self.__saldo   = saldo
        self.__limite  = limite

    def extrato(self):
        saldo_bacario = self.__saldo

        return saldo_bacario
        # print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))




    def deposita(self, valor):
        self.__saldo += valor


    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print("O VALOR {} PASSOU DO LIMITE")


    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)



    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular


    def limite(self):
        credito = self.__limite + self.__saldo
        print("Seu limite é {}que limite + {}, totaliza um saldo de {}".format(self.__saldo ,self.__limite, credito))




    @staticmethod
    def codigo_banco():
        return "001"

