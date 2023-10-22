def bubble(array):
    length=len(array)-1

    for i in range(0,length):               # 0,1,2,3,4
        for j in range(0,length):
            if array[j]>array[j+1]:
                aux=array[j]
                array[j]=array[j+1]
                array[j+1]=aux
    return array
list=[70,90,0,80,60,85]
print(bubble(list))