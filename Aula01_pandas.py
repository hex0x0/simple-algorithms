"""
Aulas básicas de Pandas

"""


import pandas as pd


data = {
        
        'alunos':['caio', 'jorge', 'pedro', 'ana', 'maria'],
        'idade':[324, 42343, 434, 34324, 3423]
        
        }



df = pd.DataFrame(data, columns=['alunos','idade'])

df.describe()

#f = df.drop([0, 1])

#df = df.drop('idade', axis=1)

#print(df['idade'].max())

#print(df['idade'].count())

#print(df['idade'].sum())

#print(df['idade'].mean())

#df = df['idade'].add(1000)

#df = df['idade'].sub(30000)

#df = df['idade'].div(10)

#df = df['idade'].mul(3)
