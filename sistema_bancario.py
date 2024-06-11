saldo = 0
saques_dia = 0
limite_saque = 500
LIMITE_SAQUES = 3

def depositar(valor):
    global saldo
    if valor > 0:
        saldo += valor
        print(f'Depósito de R${valor:.2f} realizado. Saldo atual: R${saldo:.2f}')
    else:
        print('Erro: Valor de depósito inválido.')


def sacar(valor):
    global saldo, saques_dia
    if saques_dia < LIMITE_SAQUES and valor > 0 and valor <= limite_saque and valor <= saldo:
        saldo -= valor
        saques_dia += 1
        print(f'Saque de R${valor:.2f} realizado. Saldo atual: R${saldo:.2f}')
    elif saques_dia >= LIMITE_SAQUES:
        print('Erro: Limite diário de saques atingido.')
    elif valor <= 0:
        print('Erro: Valor de saque inválido.')
    elif valor > limite_saque:
        print(f'Erro: Limite de saque é de R${limite_saque}.')
    elif valor > saldo:
        print('Erro: Saldo insuficiente para realizar o saque.')


def extrato():
    global saldo, saques_dia
    print(f'Saldo: R${saldo:.2f}')
    print(f'Saques feitos hoje: {saques_dia}')


# Função para o menu de operações
def menu():
    print("\nMenu:")
    print("1. Sacar")
    print("2. Depositar")
    print("3. Visualizar Extrato")
    print("4. Sair")

# Função principal
def main():
    while True:
        menu()
        escolha = int(input("Escolha uma opção: "))

        if escolha == 1:
            valor = float(input("Digite o valor para sacar: "))
            sacar(valor)
        elif escolha == 2:
            valor = float(input("Digite o valor para depositar: "))
            depositar(valor)
        elif escolha == 3:
            extrato()
        elif escolha == 4:
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()