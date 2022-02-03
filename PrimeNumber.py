fator = 2

n = int(input("Digite um número primo: "))

ehPrimo = True

while fator <= n // 2:
    if n % fator == 0:
        ehPrimo = False
    fator += 1

if ehPrimo:
    print(f'{n} é primo!')
else:
    print('Não é primo!')