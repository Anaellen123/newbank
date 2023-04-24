""""campo de tratamento"""
"""inscerção de dados"""

"""

'r'  -> Usado somente para ler algo
'w'  -> Usado somente para escrever algo
'r+' -> Usado para ler e escrever algo
'a'  ->  Usado para acrescentar algo

"""
valores_atribuintes = []
with open('valores_atribuintes.txt', 'w') as arquivo:
    for valor in valores_atribuintes:
        arquivo.write(str(valor) + '\n')