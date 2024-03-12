input1 = [2,3,4,5,6,7,8,9,10] #answers are none i = 5 odd length center floor divided is 4?
input2 = [-10,-8,0,3,4] #answers are i = 7 even length center floor division is 5
input3 = [0,3,4,5,6,7,8,9] #answers are i = 0
input4 = [1,2,3,4,5,6,7,8] #no right answer

input5 = [1,2,2] #answer is i = 2

def index_equals_number(array): #this is the general idea but it doesn't work, since i would need to operate on the array in place
    if len(array) < 1:
        return False
    center_index = len(array)//2
    if array[center_index] == center_index:
        return True
    else:
        return index_equals_number(array[:center_index]) or index_equals_number[array[center_index:]]
    
def split(lower, upper, array):
    center = (upper + lower) //2
    # print(array[lower:upper],lower, upper, center)
    if array[center] == center:
        return True
    elif upper - lower <= 1:
        return False
    elif array[center] > center:
        return split(lower, center,array)
    else:
        return split(center + 1, upper, array)

def idx_is_num(array):
    if len(array) == 1:
        return array[0] == 0
    else:
        center = len(array)//2
        if array[center] == center:
            return True
        return split(0,center, array) or split(center+1, len(array), array)
    

def main():
    print(idx_is_num(input5))
    if idx_is_num(input1):
        print('input 1 good')
    else:
        print('input 1 bad')
    
    if idx_is_num(input2):
        print('input 2 good')
    else:
        print('input 2 bad')

    if idx_is_num(input3):
        print('input 3 good')
    else:
        print('input 3 bad')

    if idx_is_num(input4):
        print('input 4 good')
    else:
        print('input 4 bad supposed to be bad')

if __name__ == '__main__':
    main()
