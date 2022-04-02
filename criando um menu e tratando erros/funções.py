def leiaInt1(msg):
    while True:
        try:
            n1 = int(input(msg))
        except (ValueError, TypeError):
            print('\033[33mO dado não corresponde a um número inteiro')
            continue
        except KeyboardInterrupt:
            print('\033[31m\nA leitura de dados foi interrompida pelo usuário')
            return 0
        else:
            return n1


def leiaInt2(msg):
    while True:
        try:
            n2 = int(input(msg))
        except (ValueError, TypeError):
            print('\033[33mO dado não corresponde a um número inteiro')
            continue
        except KeyboardInterrupt:
            print('\033[31m\nA leitura de dados foi interrompida pelo usuário')
            return 0
        else:
            return n2


def dividir(n1, n2):
    try:
        r = n1 / n2
    except ZeroDivisionError:
        print("\033[33mO valor nao pode ser dividido por '0'")
    else:
        print(f"O resultado de {n1} / {n2} é igual a {r:.2f}")


def somar(n1, n2):
    r = n1 + n2
    print("\033[32mA soma entre {} + {} é igual á {}".format(n1, n2, r))
    

def multiplicar(n1, n2):
    r1 = n1 * n2
    print("A multiplicação {} X {} é igual á {}!".format(n1, n2, r1))


def maior_menor(n1, n2):
    if n1 > n2:
        maior = n1
    else:
        maior = n2
    print("Entre {} e {}, o maior numero é {}:".format(n1, n2, maior))

