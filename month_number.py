dic = {
    1:'janeiro', 2:'fevereiro', 3:'março',  
    4:'abril', 5:'maio', 6:'junho', 7:'julho',
    8:'agosto', 9:'setembro', 10:'outubro', 11:'novembro',
    12:'dezembro'
}


while True:
    mes=int(input('Digite o numero do mes:'))

    if mes in dic:
        print(dic.get(mes, 0))
    