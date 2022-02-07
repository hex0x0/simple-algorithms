"""
import matplotlib.pyplot as plt

*Grafico de linhas


plt.plot([1,3, 3], [3, 4, 5], label='sala1', color='blue', linestyle='dashed')
plt.plot([3, 1, 2], [3,4,5], label='sala2', color='orange')


*Grafico de barras


import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [10, 20, 30]

plt.bar(x, y)

plt.show()






"""

import matplotlib.pyplot as plt

alunos =  ['pedro', 'maria', 'ana']
notas = [5, 10, 3]

plt.plot(notas, alunos)


plt.title('Relação notaxaluno')
plt.ylabel('Alunos')
plt.xlabel('notas')


