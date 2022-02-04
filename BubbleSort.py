
def sort(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[j] < array[i]:
                aux = array[j]
                array[j] = array[i]
                array[i] = aux

array = [9, 2, 1, 6, 3, 10]

sort(array)

print(array)






