'''class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        #print(self.x+self,y)
    
    def move(self):
        print('move')
        
    def draw(self):
        print('draw')
    
        
        
        
point1= Point()   #create object (object is blueprint of class)
point1.move()

print(point1.x)

point2=Point()  #this is different point class

#constructor 

point=Point(20,30)
print(point.x)'''

class Person:
    def __init__(self,name):
        self.name=name
        
    def talk(self):
        print(f'Hi,I am {self.name}')
    
    
john=Person('John')
john.talk()

Bob=Person('Bob')
Bob.talk()
        
