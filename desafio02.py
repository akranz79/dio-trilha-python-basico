# Funções
def depositar(saldo, extrato, valor):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(*, saldo, limite, numero_saques, extrato, LIMITE_SAQUES, valor):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques

def extrato(saldo, extrato, *, detalhado=False):
    if detalhado:
        print("\n================ EXTRATO DETALHADO ================")
        print(extrato if extrato else "Não foram realizadas movimentações.")
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=====================================================")
    else:
        print("\n================ EXTRATO ================")
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

def cadastrar_usuario(usuarios, nome, data_nascimento, cpf, endereco):
    cpf = ''.join(filter(str.isdigit, cpf))
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("CPF já cadastrado!")
            return
    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})

def criar_conta_corrente(contas, usuarios):
    agencia = "0001"
    numero_conta = len(contas) + 1
    usuario = input("Informe o CPF do usuário: ")
    for usr in usuarios:
        if usr['cpf'] == usuario:
            contas.append({'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usr['nome']})
            print("Conta criada com sucesso!")
            return
    print("Usuário não encontrado!")

# Programa principal
menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
contas = []

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(saldo, extrato, valor)

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = sacar(saldo=saldo, limite=limite, numero_saques=numero_saques, extrato=extrato, LIMITE_SAQUES=LIMITE_SAQUES, valor=valor)

    elif opcao == "3":
        detalhado = input("Deseja um extrato detalhado? (S/N): ").upper() == "S"
        extrato(saldo, extrato, detalhado=detalhado)

    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
