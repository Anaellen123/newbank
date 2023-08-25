#encapsular dados em classes
from conta import Conta

def cliente():

    limite = 100.00

    # contas de clientes já existentes
    conta001 = Conta(0o1, "Silvania", 102.89, limite)
    conta002 = Conta(0o2, "Pietro", 85.35, limite)
    conta003 = Conta(0o3, "Kaio", 256.00, limite)
    conta004 = Conta(0o4, "Samantha", 100.00, limite)


    #Cadastro de uma nova conta
    atendimento = input("Deseja realizar um cadastro? :  [sim] ou [nao]")
    while True:

        if atendimento == "sim":

            name = str(input("Informe Seu Nome :"))
            saldo = float(input("Informe Seu Saldo Bancario :"))
            numero = "0o5"

            conta005 = Conta(numero, name, saldo, limite)

            arquivo = open("registro_acesso_cliente.txt", "a")
            arquivo.write("{}, {}".format(numero, name.upper().title()) + "\n")

            arquivo.close()


            print("*****Cadastro concluido!****** ")

            while True:

                print("********Olá {}".format(name))
                print("*******DESEJA CONSULTAR SUA CONTA?*************")
                print("************OPÇÕES:\n*EXTRATO   (1)\n*SACA      (2)\n*DEPOSITAR (3)\n*TRANSFERIR(4)\n*Limite(5)\n*Acesso de conta(6)")
                system = int(input("INSIRA O NUMERO DA FUNÇÃO DESEJADA :"))


                if system == 1:

                    conta005.extrato()

                if system == 2:

                    valor_a_sacar = float(input("Você Possui {} Qual Valor Deseja Sacar? :".format(conta005.extrato())))
                    conta005.saca(valor_a_sacar)
                    print("Você sacou {} reais, Valor Restante {}".format(valor_a_sacar, conta005.extrato()))

                    continue

                if system == 3:

                    valor_a_depositar = float(input("Saldo Atual em conta {}.Qual valor Deseja Depositar? :".format(conta005.extrato())))
                    conta005.deposita(valor_a_depositar)
                    print("Você Depositou {} reais, Saldo atualizado {}".format(valor_a_depositar, conta005.extrato()))

                    continue
                #Tranferencia para contas existentes
                if system == 4:
                    print("Para Qual Conta Deseja Transferir?")
                    print("Lista De Contatos Disponíveis:\nSilvânia\nPietro\nKaio\nSamantha")
                    contato_tranferencia = str(input("Para Qual Contato Deseja Transferir? :"))

                    if contato_tranferencia == "Silvania":

                        valor_transferencia1 = float(input("O Total de Saldo Atual é{}. Quanto Deseja Transferir Para Silvânia? :".format(conta005.extrato())))
                        conta005.transfere(valor_transferencia1, conta001)
                        print("Você Transferiu {} Para Silvânia. Saldo Da Sua conta {}".format(valor_transferencia1, conta005.extrato()))

                        continue

                    if contato_tranferencia == "Pietro":

                        valor_transferencia2 = float(input("O Total de Saldo Atual é {}. Quanto Deseja Transferir Para Pietro? :".format(conta005.extrato())))
                        conta005.transfere(valor_transferencia2, conta002)
                        print("Você Tranferiu {} Para Pietro. Saldo Da Sua Conta {}".format(valor_transferencia2, conta005.extrato()))

                        continue

                    if contato_tranferencia == "Kaio":

                        valor_transferencia3 = float(input("O Total de Saldo Atual é {}. Quanto Deseja Transferir Para Kaio? :".format(conta005.extrato())))
                        conta005.transfere(valor_transferencia3, conta003)
                        print("Você Tranferiu {} Para Kaio.Saldo da Sua Conta {}".format(valor_transferencia3, conta005.extrato()))

                        continue

                    if contato_tranferencia == "Samantha":

                        valor_transferencia4 = float(input("O Total de Saldo Atual é {}. Quanto Deseja Tranferir Para Silvânia? :".format(conta005.extrato())))
                        conta005.transfere(valor_transferencia4, conta004)
                        print("Você Transferiu {} reais Para Samantha. Saldo da Sua Conta {}".format(valor_transferencia4, conta005.extrato()))

                        continue


                if system == 5:

                    conta005.limite()

                if system == 6:
                    print("****** Acessar Conta ******")
                    senha = input("Infome Sua Senha :")

                # Senha de Acesso da conta de silvania
                    if senha == "conta001":

                        arquivo = open("registro_acesso_cliente.txt", "a")
                        arquivo.write("0o1, Silvania" + "\n")

                        arquivo.close()

                        while True:

                            print("********Olá Silvania*****")
                            print("*******DESEJA CONSULTAR SUA CONTA?*************")
                            print("************OPÇÕES:\n*EXTRATO   (1)\n*SACA      (2)\n*DEPOSITAR (3)\n*TRANSFERIR(4)\n*limite (5)\n*Voltar Para Acessar outra conta(6)")
                            system_silvania = int(input("INSIRA O NUMERO DA FUNÇÃO DESEJADA :"))



                            if system_silvania == 1:

                                conta001.extrato()

                            if system_silvania == 2:

                                valor_a_sacar = float(input("Você Possui {} Qual Valor Deseja Sacar? :".format(conta001.extrato())))
                                conta001.saca(valor_a_sacar)
                                print("Você sacou {} reais, Valor Restante {}".format(valor_a_sacar, conta001.extrato()))

                                continue

                            if system_silvania == 3:

                                valor_a_depositar = float(input("Saldo Atual em conta {}.Qual valor Deseja Depositar? :".format(conta001.extrato())))
                                conta001.deposita(valor_a_depositar)
                                print("Você Depositou {} reais, Saldo atualizado {}".format(valor_a_depositar, conta001.extrato()))

                                continue

                            # Tranferencia para contas existentes
                            if system_silvania == 4:

                                print("Para Qual Conta Deseja Transferir?")
                                print("Lista De Contatos Disponíveis:\n{}\nPietro\nKaio\nSamantha".format(name))
                                conta001_transferencia = str(input("Para Qual Contato Deseja Transferir? :"))



                                if conta001_transferencia == name:

                                    valor_transferencia1 = float(input("O Total de Saldo Atual é{}. Quanto Deseja Transferir Para Silvânia? :".format(conta001.extrato())))
                                    conta001.transfere(valor_transferencia1, conta005)
                                    print("Você Transferiu {} Para Silvânia. Saldo Da Sua conta {}".format(valor_transferencia1, conta001.extrato()))

                                    continue

                                if conta001_transferencia == "Pietro":

                                    valor_transferencia2 = float(input("O Total de Saldo Atual é {}. Quanto Deseja Transferir Para Pietro? :".format(conta001.extrato())))
                                    conta001.transfere(valor_transferencia2, conta002)
                                    print("Você Tranferiu {} Para Pietro. Saldo Da Sua Conta {}".format(valor_transferencia2, conta001.extrato()))

                                    continue

                                if conta001_transferencia == "Kaio":

                                    valor_transferencia3 = float(input("O Total de Saldo Atual é {}. Quanto Deseja Transferir Para Kaio? :".format(conta001.extrato())))
                                    conta001.transfere(valor_transferencia3, conta003)
                                    print("Você Tranferiu {} Para Kaio.Saldo da Sua Conta {}".format(valor_transferencia3, conta001.extrato()))

                                    continue

                                if conta001_transferencia == "Samantha":

                                    valor_transferencia4 = float(input("O Total de Saldo Atual é {}. Quanto Deseja Tranferir Para Silvânia? :".format(conta001.extrato())))
                                    conta001.transfere(valor_transferencia4, conta004)
                                    print("Você Transferiu {} reais Para Samantha. Saldo da Sua Conta {}".format(valor_transferencia4, conta001.extrato()))

                                    continue

                            if system_silvania == 5:

                                conta001.limite()

                            if system_silvania == 6:
                                print("Acessar outra conta")
                                break
                        continue
                    # Acesso a conta de Pietro
                    if senha == "conta002":

                        arquivo = open("registro_acesso_cliente.txt", "a")
                        arquivo.write("0o2, Pietro" + "\n")

                        arquivo.close()


                        while True:
                            print("********Olá Pietro*****")
                            print("*******DESEJA CONSULTAR SUA CONTA?*************")
                            print("************OPÇÕES:\n*EXTRATO   (1)\n*SACA      (2)\n*DEPOSITAR (3)\n*TRANSFERIR(4)\n*limite (5)\n*Voltar Para Acessar outra conta(6)")
                            system_pietro = int(input("INSIRA O NUMERO DA FUNÇÃO DESEJADA :"))

                            if system_pietro == 1:

                                conta002.extrato()

                            if system_pietro == 2:

                                valor_a_sacar = float(input("Você Possui {} Qual Valor Deseja Sacar? :".format(conta002.extrato())))
                                conta002.saca(valor_a_sacar)
                                print("Você sacou {} reais, Valor Restante {}".format(valor_a_sacar, conta002.extrato()))

                                continue

                            if system_pietro == 3:

                                valor_a_depositar = float(input("Saldo Atual em conta {}.Qual valor Deseja Depositar? :".format(conta002.extrato())))
                                conta002.deposita(valor_a_depositar)
                                print("Você Depositou {} reais, Saldo atualizado {}".format(valor_a_depositar, conta002.extrato()))

                                continue

                            # Tranferencia para contas existentes
                            if system_pietro == 4:

                                print("Para Qual Conta Deseja Transferir?")
                                print("Lista De Contatos Disponíveis:\nSilvania\n{}\nKaio\nSamantha".format(name))
                                conta002_transferencia = str(input("Para Qual Contato Deseja Transferir? :"))

                                if conta002_transferencia == "Silvania":

                                    valor_transferencia1 = float(input("O Total de Saldo Atual é{}. Quanto Deseja Transferir Para Silvânia? :".format(conta002.extrato())))
                                    conta002.transfere(valor_transferencia1, conta001)
                                    print("Você Transferiu {} Para Silvânia. Saldo Da Sua conta {}".format(valor_transferencia1, conta002.extrato()))

                                    continue

                                if conta002_transferencia == name:

                                    valor_transferencia2 = float(input("O Total de Saldo Atual é {}. Quanto Deseja Transferir Para Pietro? :".format(conta002.extrato())))
                                    conta002.transfere(valor_transferencia2, conta005)
                                    print("Você Tranferiu {} Para Pietro. Saldo Da Sua Conta {}".format(valor_transferencia2, conta002.extrato()))

                                    continue

                                if conta002_transferencia == "Kaio":

                                    valor_transferencia3 = float(input("O Total de Saldo Atual é {}. Quanto Deseja Transferir Para Kaio? :".format(conta002.extrato())))
                                    conta002.transfere(valor_transferencia3, conta003)
                                    print("Você Tranferiu {} Para Kaio.Saldo da Sua Conta {}".format(valor_transferencia3, conta002.extrato()))

                                    continue

                                if conta002_transferencia == "Samantha":

                                    valor_transferencia4 = float(input("O Total de Saldo Atual é {}. Quanto Deseja Tranferir Para Silvânia? :".format(conta002.extrato())))
                                    conta002.transfere(valor_transferencia4, conta004)
                                    print("Você Transferiu {} reais Para Samantha. Saldo da Sua Conta {}".format(valor_transferencia4, conta002.extrato()))

                                    continue

                            if system_pietro == 5:

                                conta002.limite()

                            if system_pietro == 6:

                                print("Acessar outra conta")
                                break
                        continue
                    #Acesso a Conta de Kaio
                    if senha == "conta003":

                        arquivo = open("registro_acesso_cliente.txt", "a")
                        arquivo.write("0o3, Kaio" + "\n")

                        arquivo.close()

                        while True:

                            print("********Olá Kaio*****")
                            print("*******DESEJA CONSULTAR SUA CONTA?*************")
                            print("************OPÇÕES:\n*EXTRATO   (1)\n*SACA      (2)\n*DEPOSITAR (3)\n*TRANSFERIR(4)\n*limite(5)\n*Voltar Para Acessar outra conta(6)")
                            system_kaio = int(input("INSIRA O NUMERO DA FUNÇÃO DESEJADA :"))

                            if system_kaio == 1:

                                conta003.extrato()

                            if system_kaio == 2:

                                valor_a_sacar = float(input("Você Possui {} Qual Valor Deseja Sacar? :".format(conta003.extrato())))
                                conta003.saca(valor_a_sacar)
                                print("Você sacou {} reais, Valor Restante {}".format(valor_a_sacar, conta003.extrato()))

                                continue

                            if system_kaio == 3:

                                valor_a_depositar = float(input("Saldo Atual em conta {}.Qual valor Deseja Depositar? :".format(conta003.extrato())))
                                conta003.deposita(valor_a_depositar)
                                print("Você Depositou {} reais, Saldo atualizado {}".format(valor_a_depositar, conta003.extrato()))

                                continue

                            # Tranferencia para contas existentes
                            if system_kaio == 4:

                                print("Para Qual Conta Deseja Transferir?")
                                print("Lista De Contatos Disponíveis:\nSilvania\nPietro\n{}\nSamantha".format(name))
                                conta003_transferencia = str(input("Para Qual Contato Deseja Transferir? :"))

                                if conta003_transferencia == "Silvania":

                                    valor_transferencia1 = float(input("O Total de Saldo Atual é{}. Quanto Deseja Transferir Para Silvânia? :".format(conta003.extrato())))
                                    conta003.transfere(valor_transferencia1, conta001)
                                    print("Você Transferiu {} Para Silvânia. Saldo Da Sua conta {}".format(valor_transferencia1, conta003.extrato()))

                                    continue

                                if conta003_transferencia == "Pietro":

                                    valor_transferencia2 = float(input("O Total de Saldo Atual é {}. Quanto Deseja Transferir Para Pietro? :".format(conta003.extrato())))
                                    conta003.transfere(valor_transferencia2, conta002)
                                    print("Você Tranferiu {} Para Pietro. Saldo Da Sua Conta {}".format(valor_transferencia2, conta003.extrato()))

                                    continue

                                if conta003_transferencia == name:

                                    valor_transferencia3 = float(input("O Total de Saldo Atual é {}. Quanto Deseja Transferir Para Kaio? :".format(conta003.extrato())))
                                    conta003.transfere(valor_transferencia3, conta005)
                                    print("Você Tranferiu {} Para Kaio.Saldo da Sua Conta {}".format(valor_transferencia3, conta003.extrato()))

                                    continue

                                if conta003_transferencia == "Samantha":

                                    valor_transferencia4 = float(input("O Total de Saldo Atual é {}. Quanto Deseja Tranferir Para Silvânia? :".format(conta003.extrato())))
                                    conta003.transfere(valor_transferencia4, conta004)
                                    print("Você Transferiu {} reais Para Samantha. Saldo da Sua Conta {}".format(valor_transferencia4, conta003.extrato()))

                                    continue

                            if system_kaio == 5:

                                conta003.limite()

                            if system_kaio == 6:

                                print("Acessar outra conta")
                                break
                        continue
                      #Acesso a Conta de Samantha
                    if senha == "conta004":

                        arquivo = open("registro_acesso_cliente.txt", "a")
                        arquivo.write("0o4, Samantha" + "\n")

                        arquivo.close()

                        while True:
                            print("********Olá Samantha*****")
                            print("*******DESEJA CONSULTAR SUA CONTA?*************")
                            print("************OPÇÕES:\n*EXTRATO   (1)\n*SACA      (2)\n*DEPOSITAR (3)\n*TRANSFERIR(4)\n*limite(5)\n*Voltar Para Acessar outra conta(6)")
                            system_Samantha = int(input("INSIRA O NUMERO DA FUNÇÃO DESEJADA :"))

                            if system_Samantha == 1:

                                conta004.extrato()

                            if system_Samantha == 2:

                                valor_a_sacar = float(input("Você Possui {} Qual Valor Deseja Sacar? :".format(conta004.extrato())))
                                conta004.saca(valor_a_sacar)
                                print("Você sacou {} reais, Valor Restante {}".format(valor_a_sacar, conta004.extrato()))

                                continue

                            if system_Samantha == 3:

                                valor_a_depositar = float(input("Saldo Atual em conta {}.Qual valor Deseja Depositar? :".format(conta004.extrato())))
                                conta004.deposita(valor_a_depositar)
                                print("Você Depositou {} reais, Saldo atualizado {}".format(valor_a_depositar, conta004.extrato()))

                                continue

                            # Tranferencia para contas existentes
                            if system_Samantha == 4:

                                print("Para Qual Conta Deseja Transferir?")
                                print("Lista De Contatos Disponíveis:\nSilvania\nPietro\nKaio\n{}".format(name))
                                conta004_transferencia = str(input("Para Qual Contato Deseja Transferir? :"))

                                if conta004_transferencia == "Silvania":

                                    valor_transferencia1 = float(input("O Total de Saldo Atual é{}. Quanto Deseja Transferir Para Silvânia? :".format(conta004.extrato())))
                                    conta004.transfere(valor_transferencia1, conta001)
                                    print("Você Transferiu {} Para Silvânia. Saldo Da Sua conta {}".format(valor_transferencia1, conta004.extrato()))

                                    continue

                                if conta004_transferencia == "Pietro":

                                    valor_transferencia2 = float(input("O Total de Saldo Atual é {}. Quanto Deseja Transferir Para Pietro? :".format(conta004.extrato())))
                                    conta004.transfere(valor_transferencia2, conta002)
                                    print("Você Tranferiu {} Para Pietro. Saldo Da Sua Conta {}".format(valor_transferencia2, conta004.extrato()))

                                    continue

                                if conta004_transferencia == "Kaio":

                                    valor_transferencia3 = float(input("O Total de Saldo Atual é {}. Quanto Deseja Transferir Para Kaio? :".format(conta004.extrato())))
                                    conta004.transfere(valor_transferencia3, conta003)
                                    print("Você Tranferiu {} Para Kaio.Saldo da Sua Conta {}".format(valor_transferencia3, conta004.extrato()))

                                    continue

                                if conta004_transferencia == name:

                                    valor_transferencia4 = float(input("O Total de Saldo Atual é {}. Quanto Deseja Tranferir Para Silvânia? :".format(conta004.extrato())))
                                    conta004.transfere(valor_transferencia4, conta005)
                                    print("Você Transferiu {} reais Para Samantha. Saldo da Sua Conta {}".format(valor_transferencia4, conta004.extrato()))

                                    continue

                            if system_Samantha == 5:

                                conta004.limite()

                            if system_Samantha == 6:

                                print("Acessar outra conta")
                                break
                        continue




        else:
            print("resposta nâo correspondente")
            break




#fazer o arqui de registro de acesso




if(__name__ == "__main__"):

    cliente()







