'''def greet_user():    #define function
    print('welcome1')
 #after define function blank here two line   
    
greet_user()

#how to pass parameters

def function(name):   #passing parameter
    print(name)


function('welcome2')

def name(first,last):   #passing multiple parameter
    print(first,last)


name('sachith','abeywardhana')
name(last='avintha',first='sachith')  #add keyword argument

#return statement

def squre(number):
    return number*number   #using return 


print(squre(4))
print(name('sachith','avintha'))  #if you do not use return fumction autumaticaly return none.so output is none'''


def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    


n=input('Enter number:')
n=int(n)
print(f'factorial {n} = {factorial(n)}')

