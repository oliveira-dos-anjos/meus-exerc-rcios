def leiaInt(msg):
    while True:
        try:
            ni = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[33mERRO: o dado não corresponde a um valor inteiro')
            continue
        except KeyboardInterrupt:
            print('\033[31m\nA leitura de dados foi interrompida pelo usuário')
            return 0
        else:
            return ni


def leiafloat(msg):
    while True:
        try:
            nf = float(input(msg))
        except (ValueError, TypeError):
            print(f'\033[33mERRO: o dado não corresponde a um valor real')
            continue
        except KeyboardInterrupt:
            print('\033[31mA leitura de dados foi interrompida pelo usuário')
            return 0
        else:
            return nf
