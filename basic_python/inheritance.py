class Animall:                  #parent class 
        print('I am walk')


class Dog:
    def __init__(self,name):   #childern 1
        self.name=name
        print(f"I am {self.name} ")


class Cat:                     #childern 2
    def __init__(self,name):   
        self.name=name
        print(f'I am {self.name}')


lasy=Dog('lasy')
kitty=Cat('kitty')

        