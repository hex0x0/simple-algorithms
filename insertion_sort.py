array=[13, 46, 3, 13, 22, 15, 17, 41, 42, 34]


"""
46 > 13 sim




"""

def insertion_sort(array):
   
    for i in range(1, len(array)):
        chave = array[i] #46

        j = i -1

        while j >=0 and array[j] > chave:
            array[j+1] = array[j]
            j -=1

        array[j+1]=chave

    return array    





print(insertion_sort(array))
