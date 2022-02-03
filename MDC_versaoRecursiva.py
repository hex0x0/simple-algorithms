def mdc(m, n):
    if n == 0:
        return m
    return mdc(n, m % n)


print(mdc(6, 4))

print(4 % 6)