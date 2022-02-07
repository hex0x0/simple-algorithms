import matplotlib.pyplot as plt

label=['floresta', 'deserto']
dados =[31, 90]

fig, ax = plt.subplots()


ax.pie(dados, labels=label, autopct='%1.1f%%')

plt.show()

