import math
def imc(peso, altura):
    return peso / math.pow(altura, 2)




peso=float(input("Digite o seu peso (massa em kg): "))
altura=float(input("Digite a sua altura em m: "))

ret = imc(peso, altura)

if ret < 17:
    print('Muito abaixo do peso!')
elif 17 <= ret <= 18.49:
    print('Abaixo do peso!')
elif 18.50 <= ret <= 24.99:
    print('Peso normal!')
elif 25 <= ret <= 29.99:
    print('Acima do peso!')
elif 30 <= ret <= 34.99:
    print('Obesidade I')
elif 35 <= ret <= 39.99:
    print('Obesidade II (Severa)')
else:
    print('Meu amigo...')