
from datetime import datetime
def getDay(dia):
    
    if dia == 0:
        return "segunda-feira"
    elif dia == 1:
        return "terça-feira"
    elif dia == 2:
        return "quarta-feira"
    elif dia == 3:
        return "quinta-feira"
    elif dia == 4:
        return "sexta-feira"
    elif dia == 5:
        return "sábado"
    else:
        return "domingo"

verifica_veiculo = False
def Veiculos(veiculo):

    global verifica_veiculo
    
    if veiculo == "moto" or veiculo == "carro" or veiculo == "camionete":

        verifica_veiculo = True

verifica_horarios = False
def Minutos(entrada, saida):

    global verifica_horarios

    verifica_entrada = False
    verifica_saida = False

    hora = 0
    minuto = 1

    # obtemos a string do horário de entrada e "quabramos ela no meio" no char ":", criando um vetor de 2 posições
    # as horas ficam armazenados na posição 0 e os minutos ficam armazenados na posição 1
    tempo = entrada.split(":")

    # usando a função "isdigit", podemos verificar se as horas e minutos digitados são números
    if tempo[hora].isdigit() == True and tempo[minuto].isdigit() == True:

        # depois de checados, convertemos os números de string para int, para iniciarmos os cálculos
        entrada_hora = int(tempo[hora])
        entrada_minuto = int(tempo[minuto])

        # verifica se o horário de entrada está entre 8 e 17
        # se sim, significa que estamos dentro do horário de atendimento
        if entrada_hora >= 8 and entrada_hora <= 17:

            # se os minutos do horário de entrata for maior que 0 e menor ou igual a 59, está correto
            if entrada_minuto >= 0 and entrada_minuto <= 59:

                # definimos o valor da variável "verifica_entrada" como True
                # assim sabemos que podemos fazer a conversão de horas para minutos
                verifica_entrada = True
                calcula_entrada = entrada_hora * 60 + entrada_minuto
            else:
                print("err3: verifique se os minutos do horario de entrada estão corretos")
        else:
            print("err2: verifique se o horário de entrada está dentro do horário de atendimento")
    else:
        print("err1: verifique se o horário de entrada está no formato correto")

    # obtemos a string do horário de saída e executamos o mesmo método desenhado com o horário de entrada
    tempo = saida.split(":")
    if tempo[hora].isdigit() == True and tempo[minuto].isdigit() == True:

        saida_hora = int(tempo[hora])
        saida_minuto = int(tempo[minuto])

        if saida_hora >= 8 and saida_hora <= 17:

            if saida_minuto >= 0 and saida_minuto <= 59:

                verifica_saida = True
                calcula_saida = saida_hora * 60 + saida_minuto
            else:
                print("err3: verifique se os minutos do horario de saída estão corretos")
        else:
            print("err2: verifique se o horário de saída está dentro do horário de atendimento")
    else:
        print("err1: verifique se o horário de saída está no formato correto")

    # verifica se as variáveis "verifica_entrada" e "verifica saída" são True
    # se sim, ocorreu tudo certo com os calculos, e então entra no if
    if verifica_entrada == True and verifica_saida == True:
        
        if calcula_entrada < calcula_saida:

            # definimos a variável "verifica_horário" como True (isso quer dizer que os horários foram checados e está tudo certo)
            verifica_horarios = True
            
            # subtraímos o valor em minutos do horário de saída com o horário de entrada, retornado como valor da função
            return calcula_saida - calcula_entrada
        else:
            print("err4: o horário de saida é menor que o horário de entrada")

quantidade_isentos = 0
def Pagamento(minutos):
    
    global quantidade_isentos

    if minutos <= 15:
        pagamento = 0
        quantidade_isentos += 1
    
    elif minutos <= 60:
        pagamento = 1.50

    else:
        pagamento = 1.5 + int(minutos / 60 - 1)
        
    return pagamento

moto = 0
carro = 0
camionete = 0
def Dados(faturamento, quantidade_isentos):

    print(f"quantidade de veiculos: {moto} moto(s), {carro} carro(s), {camionete} camionete(s)")
    print("valor faturado até o momento: R$ {:.2f}".format(faturamento))
    print(f"quantidade de veiculos isentos: {quantidade_isentos}")

def Main():

    global verifica_veiculo
    global moto
    global carro
    global camionete

    global verifica_horarios

    faturamento = 0.0
    
    print()
    print()
    print("----- UniCesumar Parking -----")

    # obtemos o valor do "weekday" e passamos como argumento na função "getDay"
    # a função "getDay" converte o dia da semana (que está em número), e retorna o nome do dia como valor da variável "dia_semana"
    dia_semana = getDay(datetime.now().weekday())
    print(f"dia da semana: {dia_semana}")

    if dia_semana != "domingo":
        while True:
            
            print()
            cadastro = input("use: s/n _ cadastrar um novo veículo? ").lower()
            if cadastro == "s":

                print()
                veiculo = input("use: moto/carro/camionete _ tipo de veículo: ").lower()

                # chamamos a função "Veículo", passando como argumento o tipo de veículo cadastradado [linha 142]
                # a função verifica se o tipo de veículo existe na lista veículos, e retorna a variável "verifica_veículo" como True, caso esteja cadastrado
                Veiculos(veiculo)
                if verifica_veiculo == True:
                    # definimos o valor variável como False, para realizar uma nova checagem no próximo cadastro
                    verifica_veiculo = False

                    entrada = input("formato: 00:00 _ hora de entrada: ")
                    saida = input("formato: 00:00 _ hora de saída: ")

                    # passamos o horário de entrada e saída como argumentos da função "Minuto"
                    # a função "Minuto" calcula a diferença em minutos dos horários de entrada e saída e retorna o valor
                    # se estiver tudo certo com os calculos da função, a variável "verifica_horários" fica como True
                    minutos = Minutos(entrada, saida)
                    if verifica_horarios == True:
                        verifica_horarios = False

                        print()
                        print(f"tempo de permanencia: {minutos} minutos")

                        # passamos os minutos calculados na função "Minutos" como argumento na função "Pagamento"
                        # a função "Pagamento" calcula o valor a ser pago, de acordo com os minutos que o veículo ficou no estacionamento
                        # se o valor do pagamento é null, mostra a mensagem "isento de tarifa" na tela do usuário e incrementa +1 na variável "quantidade_isentos" [linha 87]
                        pagamento = Pagamento(minutos)
                        if pagamento == 0.0:
                            print("valor de cobrança: isento de tarifa")
                        else:
                            print("valor de cobrança: R$ {:.2f}".format(pagamento))
                        
                        print()
                        print("----- dados administrativos -----")

                        # pegamos o tipo de veículo cadastrado e incrementamos +1 no valor da variável correspondente
                        # esses valores são importantes para termos o controle de quantos veículos de cada tipo passou no estacionamento
                        if veiculo == "moto":
                            moto += 1
                        elif veiculo == "carro":
                            carro += 1
                        else:
                            camionete += 1

                        # armazenamos a soma de todos os valores pagos, na variável "faturamento"
                        faturamento += pagamento

                        # a função "Dados", retorna um resumo (relatório) da quantidade de veículos, valor faturado e quantidade de isenções 
                        Dados(faturamento, quantidade_isentos)
                else:
                    print("err2: tipo de veículo não cadastrado no sistema")
            
            elif cadastro == "n":

                print()
                encerrar = input("use: s/n _ deseja encerrar o programa? ").lower()
                if encerrar == "s":
                    print()
                    print("----- relatório final -----")
                    Dados(faturamento, quantidade_isentos)
                    print()
                    print("finalizado...")
                    print()
                    
                    break

                elif encerrar == "n":
                    print("continuando...")
                else:
                    print("err3: digite uma opção válida")
            else:
                print("err1: digite uma opção válida")
    else:
        print("err1: o sistema não pode ser iniciado por ser domingo")
        print()
Main()