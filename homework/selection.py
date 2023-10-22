def selection(array):
    length=len(array)-1

    for i in range(0,length):
        min_index = i
        min_value = array[min_index]

        for j in range(i,length):    # Desde el indice que comparamos

            if min_value> array[j+1]:
                min_value=array[j+1]
                min_index= j+1
        if min_index != i:
            aux=array[i]
            array[i]=array[min_index]
            array[min_index]=aux

    return array

list=[70,90,0,80,60,85]

print(selection(list))