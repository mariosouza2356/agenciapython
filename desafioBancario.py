import textwrap

def menu():
    # menu inicial
    menu = """\n
    ============== MENU =================

    [0] \t Depositos
    [1] \t Sacar
    [2] \t Extrato
    [3] \t Novo usuário
    [4] \t Nova conta
    [5] \t Listar contas
    [6] \t Sair

    =====================================
    """
    # retorna formatação da tela
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    #faz a comparação do valor se é maior que zero
    if valor > 0:
        #soma o saldo atual com o valor digitado pelo usuario
        saldo += valor
        extrato += f"Depósito:\t R$ {valor:.2f}\n"
        print("\n Depósito realizado com sucesso!")
    else:
        print("\n Operação falhou ! O valor informado é inválido.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > limite_saques


    if excedeu_saldo:
        print("\n Operção falhou ! Voce nao tem saldo suficiente.")
    elif excedeu_limite:
        print("\n Operção falhou ! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("\n Operção falhou ! Quantidade de saques diários excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\t R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso !.")
    else:
        print("\n Operção falhoe ! O valor informado é inválido.")
    return saldo, extrato

def exibir_extrato(saldo, / , *, extrato):
    print("\n============== EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\t R$ {saldo:.2f}")
    print("========================================")

def criar_usuario(usuarios):
    cpf = input("Informe op CPF (apenas números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    #verifica em usuarios se já existir cpf retorna a função principal (main)
    if usuario:
        print("\n Já existe usuário com esse CPF!")
        return
    #se não existir atribui os valores digitados pelo usuario
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimeto (dd-mm-aaaa): ")
    endereco = input("Informe o endereço  (logradouron nro - bairro - cidade/soigla estado): ")
    #adiciona o usuario a lista usuarios com o comando 'append'
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário cadastrado com sucesso !")

def filtrar_usuario(cpf, usuarios):
    #filtra o usuario     usa o laço para percorrer pelo atributo cpf
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    #retorna o primeiro cpf encontrado se já existir
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    # se o cpf já existir pula para o IF
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Conta criada com sucesso !")
        return {"agencia":agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\n Operação falhou!, Por favor reinicie o cadastro do cliente.")

def listar_contas(contas):
    #percorre a lista de contas 
    for conta in contas:
        linha = f"""\
            Agencia: \t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    # definir a variavél em uppercase é considerado valor imutavél 
    LIMITE_SAQUE = 3   
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    #laço enquanto for verdadeiro ele se repete
    while True:
        opcao = menu()

        if opcao == "0":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == "1":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                #variaveis recebendo valores de variaveis  fora do escopo 
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUE,
            )
        elif opcao == "2":
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == "3":
            criar_usuario(usuarios)
        elif opcao == "4":
            numero_da_conta = (len(contas)) + 1
            conta = criar_conta(AGENCIA, numero_da_conta, usuarios)

            if conta:
                contas.append(conta)
        elif opcao == "5":
            listar_contas(contas)

        elif opcao == "6":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()
       