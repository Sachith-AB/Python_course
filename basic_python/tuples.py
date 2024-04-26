#tupelse in python 
number = (1,2,3)  # Tuples are immutable sequences, similar to lists, but they cannot be changed after creation.

'''Certainly! Here's a brief description of tuples in Python:

Tuples are ordered collections of elements, similar to lists, but with one key difference: 
they are immutable, meaning their elements cannot be changed after creation. 
They are defined using parentheses `( )` and can contain elements of any data type, including numbers, strings, and even other tuples. 
Tuples are often used to represent fixed collections of items, such as coordinates, database records, or configurations, where immutability guarantees data integrity and prevents accidental modification.'''


coordinates = (1,2,3)

x=coordinates[0]
y=coordinates[1]
z=coordinates[2]

x,y,z = coordinates #you can define above thing using this method also

#then you can access coordinate item in anyplace using x,y,z