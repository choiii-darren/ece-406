input1 = [2,4,4,4,5,5,6,9,10] #answers are i = 5 odd length center floor divided is 4?
input2 = [1,3,5,6,7,7,7,7,7,10] #answers are i = 7 even length center floor division is 5
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
    else:
        ret1 = split(lower, center, array)
        ret2 = split(center+1, upper, array) #prob how the array length is differenet or the base case
        return ret1 or ret2 #being floor divided so center cannot equal len(array)

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
