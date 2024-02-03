array = []
for i in range(21):
    array.append(14*i)
for num in array:
    if num % 21 == 14:
        print(num)
    if num % 21 == 15:
        print('found')