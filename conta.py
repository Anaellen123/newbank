class Conta:
    def __init__ (self,numero, titular, saldo, limite):
        print("construindo objeto...{}".format(self))
        self.__numero  = numero
        self.__titular = titular
        self.__saldo   = saldo
        self.__limite  = limite

