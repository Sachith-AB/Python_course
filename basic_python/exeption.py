#using to handle errors

try:
    age=int(input('Age:'))   #input is correct
    print(age)
except ValueError:    # input is wrong
    print('Invalid value')

try:
    age=int(input('Age:'))
    income=120000
    risk=income/age
    print(age)
except ZeroDivisionError:
    print("age can not be zero")
except ValueError:
    print('Invalid value')
    
