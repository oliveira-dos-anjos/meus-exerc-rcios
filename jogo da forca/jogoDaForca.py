import random

# import os
def jogar():
    imprimi_mensagem_de_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = letras_acertadas_com_(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    print(f'\n\033[34m{letras_acertadas}')

    while not enforcou and not acertou:
        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)

        #                os.system('cls')
        else:
            erros += 1
        #             os.system('cls')
        enforcou = erros == 5
        acertou = '_' not in letras_acertadas
        print('\n')
        print(f'\033[34m{letras_acertadas}')
        print(f'\n\033[31mErros : {erros} / 5')

    if (acertou):
        Imprimir_mensagem_vencedor()
    else:
        Imprimir_mensagem_perdeu(palavra_secreta)

    print('\033[4;31mFim do jogo')


def imprimi_mensagem_de_abertura():
    print('\033[32m*********************************')
    print('***\033[33mBem vindo ao jogo da Forca!\033[32m***')
    print('*********************************')


def carrega_palavra_secreta():
    try:
        arquivo = open('palavras.txt', 'rt')
    except FileNotFoundError:
        return False
    else:
        palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def letras_acertadas_com_(palavra_secreta):
    return ['_' for letra in palavra_secreta]


def pede_chute():
    chute = input("\033[32mQual letra? ")
    chute = chute.strip().upper()
    return chute


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    posição = 0
    for letra in palavra_secreta:
        if (chute.upper() == letra.upper()):
            letras_acertadas[posição] = letra
        posição = posição + 1


def Imprimir_mensagem_vencedor():
    print('\033[33mParabéns, você ganhou!\033[35m')
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def Imprimir_mensagem_perdeu(palavra_secreta):
    print('\033[33mPuxa, você foi enforcado!')
    print('\033[31mA palavra era \033[32m{}'.format(palavra_secreta))
