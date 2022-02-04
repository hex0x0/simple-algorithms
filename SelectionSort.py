
def sort(array):
    for i in range(len(array)):
        min_index=i
        for j in range(i+1, len(array)):
            if array[j] < array[min_index]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]

array = [9, 2, 1, 6, 3, 10]

sort(array)

print(array)



