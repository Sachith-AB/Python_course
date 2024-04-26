#while loop
'''i=0    
while i<5:  #when this condition is false this while loop working
    print(i)
    i=i+1
print('Done') #after working loop

i=0
while i<5:  
    print('*'*i)
    i=i+1'''

#for loop

'''for item in 'python': #print letter one by one
    print(item)
    
for item in ['sachith','avintha','abeywardhana']: #print word one by one
    print(item)
for item in range(10):  #print 0 to 9
    print(item)
for item in range(3,10):  #print 5 to 9
    print(item)
for item in range(5,10,2): #print item increment two hy two
    print(item)
# total of array element using for loop   
total=0
prices=[10,20,30]
for i in prices:
    total=total+i
    
print(total)'''

#nested loop
'''for x in range(2):   #coordinates are in range 2
    for y in range(2):
        print(f'{x,y}')'''
        
# using one for loop create 'F'
number=[5,2,5,2,2]
'''for i in number:
    print('x'*i)'''
    
#using two for loop create 'F'
for j in number:
    output=" "
    for k in range(j):
        output=output + 'x'
    print(output)
           
        
       
       
        
    
  
        

    
   
