atual = 0
proximo = 1
aux = 0

v = int(input("Digite até que posição deseja testar:"))

x = 0

while x < v:
    print(atual)
    aux = atual + proximo
    atual = proximo
    proximo = aux
    x += 1
  