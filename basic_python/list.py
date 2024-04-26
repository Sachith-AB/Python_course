names=['sachith','avinth','abeywardhana']  #define list 
print(names)   #print all element in list
print(names[0])   #print special element in list
print(names[-1])   #print end element in list
print(names[2:])  #elemen in index 2 to end
print(names[0:2])  #element index 0 to index 2 
names[0]='sahan'
print(names)

#get largest number in list

numbers = [11,3,6,2,8,4,10]
max=numbers[0]

for i in numbers:
    if max<i:
        max=i
   
print(max)

#2 dimensional list in python

matrix=[[1,2,3],[4,5,6],[7,8,9] ]    #define 2d list
print(matrix)    #print all element in list
print(matrix[1][1])  #print special element in list

#getting all element in matrix 

for row in matrix:
    for item in row:
        print(item)
        
#method in list

numbers=[1,2,3,5,6,7,8,9]

numbers.append(10)  #add new element in end of the list
print(numbers)

numbers.insert(3,4)  #add special place to element
print(numbers)

numbers.pop() #remove last element in list
print(numbers)

print(numbers.index(5))   #search number in index 5
print(50 in numbers)  #search number in index 50 get boolean value

print(numbers.count(5))   #count element 5 in list

numbers.sort() #sorted list to decending order
numbers.reverse()  #sorted list to accending order

numbers2=numbers.copy()  #copy list to another
numbers.append(10)   #add element to numbers
print(numbers2)     #but not add it to numbers2 list
 

numbers.clear()   #clear all the item in list
print(numbers) 

#remove duplicate value in array

array=[11,34,11,56,11,56,78,34,11,34,89,90]
array.sort()
print(array)

unique=[]
for i in array:
    if i not in unique:
        unique.append(i)
print(unique)

