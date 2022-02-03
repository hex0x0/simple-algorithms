fator = 2

n = 12


while n > 1:
    if (n % fator) == 0:
        print(f"Fator = {fator}")
        n = n//fator
    else:
        fator += 1



