from time import sleep

def menu():
    sleep(1)
    print("\033[35m==" * 20)
    print("\033[33m{:^40}".format('MENU PRINCIPAL'))
    print("\033[35m==" * 20)
    print('\033[33m1 - \033[34mVer pessoas cadastradas')
    print('\033[33m2 - \033[34mCadastrar novas pessoas')
    print('\033[33m3 - \033[34mSair do sistema')
    print("\033[35m==" * 20)
    n = leiaInt('\033[33mSua opção: ')
    return n


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO: o valor nao corresponde a um numero")
        except UnboundLocalError: 
            print("\033[31mERRO: o valor nao corresponde a um numero")
        except KeyboardInterrupt:
            print("\033[31mA leitura de dados foi interrompida pelo usuário")
        else:
            if n == 1 or n == 2 or n == 3:
                return n
            else:
                print('\033[31mERRO: o valor nao corresponde a uma das opções:')


def leiaIdade(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO: o valor nao corresponde a um numero")
        except KeyboardInterrupt:
            print("\033[31mA leitura de dados foi interrompida pelo usuário")
        else:
            return n
            

def pessoas():
    sleep(1)
    print("\033[35m==" * 20)
    print("\033[33m{:^40}".format("PESSOAS CADASTRADAS"))
    print("\033[35m==" * 20)


def cadastrar():
    sleep(1)
    print("\033[35m==" * 20)
    print("\033[33m{:^40}".format("CADASTRAR NOVAS PESSOAS"))
    print("\033[35m==" * 20)


def sair():
    sleep(1)
    print("\033[35m==" * 20)
    print("\033[33m{:^40}".format("SAINDO DO SISTEMA... ATÉ LOGO!"))
    print("\033[35m==" * 20)
    print('\033[m', end= '')
