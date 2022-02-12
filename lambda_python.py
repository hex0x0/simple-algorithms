#aula41 -> lambdas

"""
O lambda precisa de uma variável containner para

realizar a operação



"""

f = (lambda x, y, z: x+y+z)


print(f(1, 2, 3))


fibo = (lambda x, y, z: x*y*z)


clo = (lambda x: lambda y: x+y)

e = clo(3)
print(e(2))





print(fibo)



print(fibo(3, 2, 3))









