from dependências.funções import *

def ArquivoExist(arq):
    try:
        a = open(arq, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
  
    
def Criar_Arq(arq):
    try:
        a = open(arq, 'wt+')
        a.close()
    except:
        print('\033[31mHouve um erro na criação do arquivo!')
    else:
        print(f'\033[32mArquivo \033[33m{arq} \033[32mcriado com sucesso!')


def LerArquivo(arq):
    try:
        a = open(arq, "rt")
    except:
        print("Erro ao ler o arquivo")
    else:
        pessoas()
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace("\n", "")
            print(f"\033[33m{dado[0]:<30}{dado[1]:>5} anos")
    finally:
        a.close()
    
def cadastro(arq, nome="Desconhecido", idade=0):
    try:
        a = open(arq, 'at')
    except:
        print("\033[31mHouve um erro ao carregar o arquivo!")
    else:
        try:
            a.write(f"{nome};{idade}\n")
        except:
            print("Houve um erro ao carregar o arquivo")
        else:
            print(f'\033[33mNovo registro de \'{nome}\' adicionado.')
            a.close()
