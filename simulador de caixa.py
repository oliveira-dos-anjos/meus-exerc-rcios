from time import sleep
while True:
    print("\033[1;32mOlá! seja bem vindo a loja\033[m")
    print("\033[1;32mBoas compras\033[m")
    PRODUTO = float(input("\033[1;31mQual o valor do produto? R$\033[m"))
    sleep(1)
    print("""\033[0;33mQual a forma de pagamento?\033[4;32m
    [0] CHEQUE
    [1] DINHEIRO
    [2] CARTÃO\033[m""")
    sleep(1)
    OPCAO = int(input("\033[1;31mINFORMA UMA DAS OPÇÕES ACIMA "))
    sleep(1)
    if OPCAO == 0:
        P0 = PRODUTO - PRODUTO * 10 / 100
        print("\033[1;33mVoçê recebeu 10% de desconto!\033[m")
        sleep(1)
        print("\033[1;32mO valor a ser pago é de R${:.2f}!\033[m".format(P0))
    elif OPCAO == 1:
        P1 = PRODUTO - PRODUTO * 10 / 100
        print("\033[1;33mVoçê recebeu 10% de desconto!\033[m")
        sleep(1)
        print("\033[;32mO valor a ser pago é de R${:.2f}!\033[m".format(P1))
        sleep(1)
        print("""\033[1;35mPrecisa de troco?\033[1;32m
        [1] NÃO
        [2] SIM\033[m""")
        sleep(1)
        opcao = int(input("\033[0;31mINFORME UMA DAS OPÇÕES ACIMA\033[m "))
        if opcao == 2:
            sleep(1)
            VT = int(input("\033[0;35mPara qual valor voçê precisa de troco?\033[m "))
            T = VT - P1
            sleep(1)
            print("\033[1;32mSeu troco é de R${:.2f}\033[m".format(T))
    elif OPCAO == 2:
        print("""\033[1;33mComo gostaria de pagar?\033[1;32m
        [1] A VISTA COM 5% DE DESCONTO.
        [2] EM 2X SEM JUROS.
        [3] EM 3X OU MAIS\033[m""")
        sleep(1)
        pagamento = int(input("\033[1;33mINFORME UMA DAS OPÇÕES ACIMA \033[m"))
        sleep(1)
        if pagamento == 1:
            UMA = PRODUTO - PRODUTO * 5 / 100
            print("\033[0;33mVoçê tem 5% de desconto! \033[m")
            sleep(1)
            print("\033[1;32mO valor da compra será de {:.2f}!!!".format(UMA))
        elif pagamento == 2:
            parcela2 = PRODUTO / 2
            print("\033[1;32mVoçê pagará duas parcelas de R${:.2f}\033[m ".format(parcela2))
        elif pagamento == 3:
            print("\033[1;31mNesta opção voçê pagará 20% de juro\033[m")
            N = int(input("\033[1;34mQuantas parcelas gostaria de pagar?\033[m"))
            parcela3 = (PRODUTO + (PRODUTO * 20) / 100) / N
            sleep(1)
            print("\033[1;32mVoçê pagará {} parcelas de R${:.2f}\033[m ".format(N, parcela3))
    comprar_novamente = str(input('Deseja fazer outra compra? [S/N]: ')).upper().strip()
    if comprar_novamente == "N":
        break
sleep(1)
print("\033[1;31;40mPARABÉNS PELA COMPRA\033[m")
