
def collatzSequence(n):
    

    print(n)
    
    if n == 1:
        return n
    elif n % 2 == 0:
        return collatzSequence(n // 2)
    elif n % 2 == 1:
        return collatzSequence(3*n+1)
        
    
    

try:
    value = int(input("Digite um número inteiro:"))
    collatzSequence(value)
except:
    print("Valor digitado não é um tipo int")


    


