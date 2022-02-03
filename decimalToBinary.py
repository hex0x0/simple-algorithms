


def decimalToBinary(n):
    bin = 0
    bit = 0
    pot = 1
    while n > 0:
        bit = n % 2
        n //= 2
        bin = bin + (bit*pot)
        pot = pot * 10

    return bin



print(decimalToBinary(1024))
