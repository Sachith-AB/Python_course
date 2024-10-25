number = [11,3,6,2,8,4,0]

# Initialize max and second_max to very small values
max = float('-inf')
second_max = float('-inf')

for i in number:
    if i > max:
        # Update second_max before updating max
        second_max = max
        max = i
    elif i > second_max and i != max:
        # Update second_max if i is smaller than max but larger than second_max
        second_max = i

# print(second_max)

#buble sort
my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)

def bubleSort(n,my_array):
    
    for i in range(n-1):
        for j in range(n-i-1):
            if my_array[j] > my_array[j+1]:
                my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
    return my_array


print("Sorted array:", bubleSort(n,my_array))        