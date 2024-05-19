#Deposito, saque e extrato.

#Depósito: adicionar valores inteiro e positivos (OK)

#Saque: máximo 3 saques diários(OK)
#limite 500 reais por saque. (OK)
#Sem saldo deve exibir mensagem de que não é possível sacar(OK)

#Extrato: listar todos os depósito e saques realizados na conta
#No final informar sado atual (OK)
#Formato R#1500.45(OK)

novo_valor = float(0)
quantidade_saque = float(0)
lista = list()

def sistema_bancario():

    operacao = input("Informe a operação que deseja realizar: \n[D] para depósito \n[S] para saque \n[E] para extrato \n[Q] para sair\n")

    if operacao == "D":

        deposito = float(input("Inserir o valor que deseja depositar: "))
        global novo_valor
        novo_valor = novo_valor + deposito
        print(f"O valor R${deposito:.2f} foi depositado \n")
        lista.append(deposito)
        return sistema_bancario()
    
    elif operacao == "S":

        saque = float(input("Inserir o valor que deseja sacar: "))
        if novo_valor>=saque:
            global quantidade_saque
            quantidade_saque += 1

            while quantidade_saque <=3:
                if saque <=500:
                    novo_valor = novo_valor - saque
                    print(f"O valor R${saque:.2f} foi retirado \n")
                    lista.append(-saque)
                    return sistema_bancario()

                else:
                    print("O valor máximo de saque permitido é R$500,00 \n")
                    return sistema_bancario()
            print("Quantidade de saque diária excedida \n")
            return sistema_bancario()
        else:
            print("Valor do saque superior ao saldo disponível \n")
            return sistema_bancario()
    elif operacao == "E":
        print(f"Saldo: R${novo_valor:.2f} \n")
        print("Entradas e saídas:")
        for valor in lista:
            print(f'R${valor:.2f}')
        return sistema_bancario()
    elif operacao == "Q":
        print("Você decidiu sair \n")
    else:
        print("Operação invalida, por favor inserir a operação desejada.\n")
        return sistema_bancario()

sistema_bancario()