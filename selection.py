import random

def split(array, integer):
    index = 0
    for i in range(len(array)):
        if array[i] < integer:
            temp = array[i]
            array[i] = array[i+1]
            array[i+1] = temp
            index += 1
    a = index
    for i in range(index, len(array)):
        if array[i] == integer:
            temp = array[i]
            array[i] = array[i+1]
            array[i+1] = temp
            index += 1
    b = index
    return (a,b)

def selection(array, k):
    if array[-1] == 1:
        return array[0]
    randomInt = random.randint(0,len(array)-1)
    integer = array[randomInt]
    (a,b) = split(array, integer)
    if k < a:
        return selection(array[:a], k)
    elif k > b:
        return selection(array[b+1:],k-b)
    else:
        return integer