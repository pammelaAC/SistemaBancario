#Desafio 2

#Criar usuário:
#Nome
#Data de nascimento
#CPF
# Endereço

#Criar conta
#Agência (0001)
#Número da conta (1000, 1001...)
#usuário

#Fazer a busca por CPF

conta = 0

def sistema_bancario():

    novo_valor = float(0)
    quantidade_saque = float(0)
    saque_maximo = 500
    AGENCIA = "0001"
    lista = list()
    lista_cpf = {
        'Nome': [],
        'Data de nascimento': [],
        'CPF': [],
        'Endereço': [],
        'Conta': []
    }

    while True:

        operacao = input("Informe a operação que deseja realizar: \n[D] para depósito \n[S] para saque \n[E] para extrato \n[NU] para criar usuário \n[NC] para criar nova conta \n[Q] para sair\n")

        if operacao == "NU":
            lista_cpf = criar_usuario(lista_cpf)

        elif operacao == "NC":
            lista_cpf = nova_conta(lista_cpf)

        elif operacao == "D":
            novo_valor, lista = deposito(novo_valor, lista)

        elif operacao == "S":
            novo_valor, lista, quantidade_saque = saque(novo_valor, quantidade_saque, saque_maximo, lista)

        elif operacao == "E":
            extrato(novo_valor,lista)

        elif operacao == "Q":
            print("Você decidiu sair \n")
            break
        else:
            print("Operação invalida, por favor inserir a operação desejada.\n")


def criar_usuario(lista_cpf):
    nome = input("Informe a nome do novo usuário: ")
    data_nacimento = input("Informe a data de nascimento: ")
    cpf = input("Informe o cpf: ")
    endereco = input("Informe endereço: ")

    if cpf in lista_cpf['CPF']:
        print("\nUsuário já existe. Favor digitar outro CPF\n")
    else:
        lista_cpf['Nome'].append(nome)
        lista_cpf['Data de nascimento'].append(data_nacimento)
        lista_cpf['CPF'].append(cpf)
        lista_cpf['Endereço'].append(endereco)
        lista_cpf['Conta'].append([])
        print('\nUsuário criado com sucesso! \n')

    return lista_cpf

def nova_conta(lista_cpf):
    global cpf_conta
    cpf_conta = input("Digite o CPF do usuário que deseja criar a conta: ")

    if cpf_conta in lista_cpf['CPF']:
        global conta
        conta +=1
        index = lista_cpf['CPF'].index(cpf_conta)
        lista_cpf['Conta'][index].append(conta)  
        print(f'\nNova conta criada com sucesso! Agência: 0001. Conta: {conta}.\n')

    else:
        print("CPF não encontrado, favor digitar um CPF valido ou criar um usuário")
    return lista_cpf

def deposito(novo_valor, lista):
    deposito = int(input("Inserir o valor que deseja depositar: "))
    novo_valor += deposito
    print(f"O valor R${deposito:.2f} foi depositado \n")
    lista.append(deposito)
    return novo_valor, lista
    
def saque(novo_valor, quantidade_saque, saque_maximo, lista):
    saque = float(input("Inserir o valor que deseja sacar: "))
    if novo_valor>=saque:
        
        if quantidade_saque <3:
            if saque <= saque_maximo:
                novo_valor -= saque
                quantidade_saque += 1
                print(f"O valor R${saque:.2f} foi retirado \n")
                lista.append(-saque)
                
            else:
                print("O valor máximo de saque permitido é R$500,00 \n")
        else:
            print("Quantidade de saque diária excedida \n")
    else:
        print("Valor do saque superior ao saldo disponível \n")
    return novo_valor, lista, quantidade_saque
    
def extrato(novo_valor,lista):
    print(f"Saldo: R${novo_valor:.2f} \n")
    print("Entradas e saídas:")
    for valor in lista:
        print(f'R${valor:.2f}')

    
    
sistema_bancario()

