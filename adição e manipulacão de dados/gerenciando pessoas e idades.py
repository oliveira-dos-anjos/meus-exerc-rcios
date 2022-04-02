from dependências.funções import *
from dependências.arquivo import *

arq = 'tentando_um_mini_banco_de_dados'
if not ArquivoExist(arq):
    Criar_Arq(arq)

while True:
    n = menu()
    if n == 1:
        # opção para ler um arquivo
        LerArquivo(arq)
    if n == 2:
        # opção para cadastrar novas pessoas
        cadastrar()
        nome = str(input('\033[32mDigite o nome: '))
        idade = leiaIdade('Digite a idade: ')
        cadastro(arq, nome, idade)

    if n == 3:
        sair()
        break

