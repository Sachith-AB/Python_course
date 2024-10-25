
numbers = [10,3,5,7,2]
sorte = [1,2,3,4,5,6]

n = len(numbers)

def sortNumbers(numbers,n):
    for i in range(n): 
        for j in range(n-1): 
            if numbers[j] > numbers[j+1]:
                k = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = k
    return numbers        

def maxNumbers(numbers):
    max = 0
    for i in range(len(numbers)):
        if(numbers[i] > max):
            max = numbers[i]
    return max

def minNumbers(numbers):
    min = numbers[0]
    for i in range(len(numbers)):
        if(numbers[i] < min ):
            min = numbers[i]
    return min

def secondMax(numbers):
    max = 0
    max_2 = 0
    for i in range(len(numbers)):
        if(numbers[i] > max):
            max = numbers[i]
    
    for i in range(len(numbers)):
        if(numbers[i] > max_2 and numbers[i] < max):
            max_2 = numbers[i]
    return max_2

def secondMin(numbers):
    min = numbers[0] 
    min_2 = numbers[0]    
    
    for i in range(len(numbers)):
        if(numbers[i] < min ):
            min = numbers[i]
            
    for i in range(len(numbers)):
        if(min < numbers[i] < min_2):
            min_2 = numbers[i]
    return min_2

def reversArray(numbers):
    revers = []
    
    for i in range(len(numbers) - 1  , -1 , -1):
        
        revers.append(numbers[i])
        
    print(revers)
    
def checkSorted(numbers):
    temp = numbers[:]
    for i in range(n): 
        for j in range(n-1): 
            if numbers[j] > numbers[j+1]:
                k = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = k
    
    for i in range(n):
        if(numbers[i] == temp[i]):
            return True
        else:
            return False

def rotateArray(numbers , k):
    temp = numbers[:]
    for i in range(len(numbers)):
        j = (i+k)% len(numbers)
        numbers[j] = temp[i]
    print(numbers) 

print(checkSorted(sorte))