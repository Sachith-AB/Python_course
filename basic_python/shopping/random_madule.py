import  random

'''i=0
for i in range(3):
    print(random.randint(4,20))   #this give random 3 value between 4 to 10'''


'''members=['sachith','sahan','avintha','abeywardhana']
print(random.choice(members))'''

#dice roll randomly
class Dice:
    def roll(self):
        first = random.randint(1,6)
        second=random.randint(1,6)
        return (first,second)


dice=Dice()
print(dice.roll())
        
   





