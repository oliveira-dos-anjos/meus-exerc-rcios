from time import sleep
from funções import *
n1 = leiaInt1("\033[32mdigite um valor: ")
n2 = leiaInt2("digite outro valor: ")
opcao = 0
maior = 0
while opcao != 6:
    print('\033[35mO que deseja fazer com os valores informados?')
    sleep(1)
    print("\033[36m==-==" * 10)
    print("""    \033[33m[1] somar
    [2] multiplicar
    [3] maior
    [4] dividir
    [5] novos numeros
    [6] sair do programa""")
    print("\033[36m==-==" * 10)
    sleep(1)
    opcao = int(input("\033[32mDigite uma das opções: "))
    sleep(1)
    if opcao == 1:
       somar(n1, n2)
    elif opcao == 2:
        multiplicar(n1,n2)
    elif opcao == 3:
        maior_menor(n1, n2)
    elif opcao == 4:
        dividir(n1, n2)
    elif opcao == 5:
        n1 = leiaInt1("\033[33mdigite outro numero: ")
        n2 = leiaInt2("digite outro numero novamente: ")
    elif opcao == 6:
        print("\033[31msaindo...")
        sleep(1)
    else:
        print("Entrada inválida")
        sleep(1)
print("fim\033[m")
