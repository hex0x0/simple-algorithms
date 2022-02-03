


def binaryToDecimal(n):
    dec = 0
    bit = 0
    pot = 1
    while n > 0:
        bit = n % 10
        n //= 10
        dec = dec + (bit*pot)
        pot = pot * 2

    return dec



print(binaryToDecimal(1000))









