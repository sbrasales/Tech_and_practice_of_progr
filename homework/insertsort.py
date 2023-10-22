def insert(array):
    lenght=len(array)

    for i in range(1,lenght):
        i_value= array[i]
        i_index= i

        while i_index > 0 and array[i_index - 1] > i_value:
            array[i_index]=array[i_index - 1]
            i_index -= 1
        array[i_index] = i_value
    return array

list=[70,90,0,80,60,85]
print(insert(list))