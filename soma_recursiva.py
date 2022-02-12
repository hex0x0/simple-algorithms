#N -> soma recursiva de n até 0


def soma_recursiva(n):
    if n == 0:
        return 0
    else:
        return n + soma_recursiva(n-1)



print(soma_recursiva(4))