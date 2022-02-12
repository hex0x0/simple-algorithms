saldo_positivo = 0
contas = []
depositos = []


def main():
    

    op = bool(int(input('Deseja criar conta(1) ou sair(0) :')))

    while op:
        criar_conta()
        ver_saldo()
        op = bool(int(input('Deseja criar conta(1) ou sair(0) :')))



def criar_conta():
    
    global saldo_positivo, contas, depositos
    num_conta = int(input('Digite um numero de conta:'))
    while num_conta in contas:
        print("Numero já existe")
        num_conta = int(input('Digite um numero de conta:'))
    
    contas.append(num_conta)

    deposito = float(input('Digite um valor de deposito:'))


    while deposito <= 0:
        print('Deposito invalido')
        deposito = float(input('Digite um valor de deposito:'))

    depositos.append(deposito)

    saldo_positivo += deposito



def ver_saldo():
    global saldo_positivo

    op = bool(int(input('Digite (1 - para ver saldo e 0 - para sair) ')))

    if op:
        print('Saldo: %i'%saldo_positivo)



main()