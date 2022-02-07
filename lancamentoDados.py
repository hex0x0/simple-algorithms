#dados
import random

array=[]

for i in range(100):
    rd = random.randint(1, 6)

    array.append(rd)


for i in range(1, 7):
    print('O numero {} aparece {}'.format(i, array.count(i)))
