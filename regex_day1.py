"""
    https://www.knowledgeisle.com/wp-content/uploads/2020/01/Al-Sweigart-Automate-The-Boring-Stuff-With-Python_-Practical-Programming-For-Total-Beginners-No-Starch-Press-2019.pdf






import re

phone_expression = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')

mo = phone_expression.search('My number is 414-155-4242')
# passe valores 1, 2, 3 como parametro de mo.group()
print('Phone number found: ' + mo.group())

# passe valores 1, 2, 3 como parametro de mo.group()
#mo.groups() retorna uma tupla


areaCode, mainNumber = mo.groups()

print(areaCode, mainNumber)


Escapando parênteses


phone_expression = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')

mo = phone_expression.search('My number is (414) 155-4242')
# passe valores 1, 2, 3 como parametro de mo.group()
#mo.groups() retorna uma tupla


print(mo.group(1))
print(mo.group(2))



Utilizando o caractere | chamado de pipe

Usamos ele quando queremos fazer a correspondência de uma entre várias expressões

phone_expression = re.compile(r'Batman|Tina Fey')

match = phone_expression.search('Tina Fey')


print(match.group())


***


batRegex = re.compile(r'Bat(man|mobile|copter|bat)')

mo = batRegex.search('Batbat')

print(mo.group())

ou


print(mo.group(1))


(char)? a expressão entre parênteses é opcional

batRegex = re.compile(r'Bat(wo)?man')

mo = batRegex.search('Batwoman')

print(mo.group())

A regex corresponderá a expressões que contenham nenhuma ou pelo menos 1
ocorrência de wo


***

Escapando o ponto de interrogação

batRegex = re.compile(r'Bat(wo)?man\?')

mo = batRegex.search('Batwoman?')

print(mo.group())



***

Utilizando o asterisco

Para 'Batman?', a parte referente a (wo)* corresponde a 0 ocorrÇencias de wo
Para 'Batwoman?', (wo)* corresponde a uma ocorrência

* -> corresponda a 0 ou mais

*******

O + quer dizer corresponda a um ou mais ocorrências


batRegex = re.compile(r'Bat(wo)+man\?')

mo = batRegex.search('Batwowowoman?')

print(mo.group())

Retorna None se não houve correspondência

***

Repetição usando chaves {}

import re

batRegex = re.compile(r'(Ha){3}')

mo = batRegex.search('HaHaHa?')

print(mo.group())

3 ou mais ocorrências
----------------------------

batRegex = re.compile(r'(Ha){3,}')

0 a três ocorrências

--------------------------


batRegex = re.compile(r'(Ha){,3}')



****


findall()

Retorna uma lista de strings - desde que não haja grupos na expressão regular

phone_regex = re.compile(r'd\d\d-\d\d\d-\d\d\d\d')



mo  = phone_regex.findall('Cell: 415-554-9994 Work: 212-555-0000')

print(mo)


Se houver grupos na expressão regular, findall() retornará uma lista de tuplas

Cada tupla representa uma correspondência e seus itens serão as strings correspondentes
a cada grupo da regex


ex.1
phone_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

mo = phone_regex.findall('222-333-4444')

print(mo)

ex.2

phone_regex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')

mo = phone_regex.findall('222-333-4444')

print(mo)

Correspondência para placa de carro

phone_regex = re.compile(r'\D{3}-\d{4}')

mo = phone_regex.findall('JKF-3495')

\d - qualquer digíto de 0 a 9
\D qualquer caracter que não seja um dígito de 0 a 9
\w caracteres de "palavra"

phone_regex = re.compile(r'\d{3}.\d{3}.\d{3}-\d{2}')

mo = phone_regex.findall('029.950.301-13')

if len(mo) != 0:
    print('Corresponde')
    
\w caracteres de 'palavra'

\W qualquer caracter que não seja uma letra, um dígito ou o underscore

\s espaço

\S qualquer caractere que não seja um espaço, uma tabulação ou uma quebra de linha



phone_regex = re.compile(r'\d+\s\w+')

mo = phone_regex.findall('32 pipes')

print(mo)

Criando nossas próprias classes de caracteres usando colchetes

phone_regex = re.compile(r'[aeiouAEIOU]')

mo = phone_regex.findall('esse mundo e grande')


for i in mo:
    print(i)


Também é possível incluir intervalos de letras ou de números

phone_regex = re.compile(r'[a-zA-Z0-9]')

^ o circunflexo é negação desse intervalo

consonant_regex = re.compiler(r'[^aeiouAEIOU]')

Retorna uma tupla de consoantes

O acento circunflexo também pode ser usado no início da regex para indicar que
uma correspondência deve ocorrer no início de um texto pesquisado.


phone_regex = re.compile(r'[^a-zA-Z0-9]')

-> $#***


beginsWithHELLO = re.compile(r'^HELLO')

print(beginsWithHELLO.search('HELLO WORLD'))

$ -> indica que a ocorrência acontece no final


endsWith = re.compile(r'\d$')

mo = endsWith.search('ola123')

print(mo)

O ponto . é chamado caractere-curinga e corresponde a qualquer caractere, exceto
uma quebra de linha


"""

import re

endsWith = re.compile(r'\d$')

mo = endsWith.search('ola123')

print(mo)