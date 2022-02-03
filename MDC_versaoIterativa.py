m = 4
n = 6

while n > 0:
    aux = n
    n = m % n
    m = aux



print(f"MDC = {m}")