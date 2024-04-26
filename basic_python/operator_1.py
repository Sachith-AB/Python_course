#logical operator
has_high_income = True
has_good_credit = True
has_criminal_record = True

if has_high_income and has_good_credit:  #using and oprator both should be true
    print('Eligibale loan')
    
if has_good_credit or has_high_income:  #using or opratorn at least one should be true
    print('Eligibale loan')
if has_high_income and not has_criminal_record:   #using not opeator
    print('Eligibale loan')
    
#comparision operator

temperture = 30

if temperture>30:   
    print('Hot day')
    
elif temperture==30:
    print('Hot day')
    
else:
    print('Cold day')
    
name=input("Enter Your Name:")

if len(name)<3:
    print('Name should be minium 3 character')
elif len(name)>50:
    print('Name should be maximum 50 character')
else:
    print('Name looks Good')

#weight converter

weight=input("Enter your weight:")
unit=input("'Kg'(1)/'lbs'(2):")

if int(unit)==1:
    weight=float(weight)*2.20462
    print(f"weight={weight}lbs")
elif int(unit)==2:
    weight=float(weight)/2.20462
    print(f"weight={weight}kg")
else:
    print('Your input is wrong')
    



    

    


