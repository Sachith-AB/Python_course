#define dictionaries in python

customer ={
    "name":'Sachith Avintha',
    'age':22,
    'is_verified':True
}

print(customer['name'])  #acces in out item in dictionries
print(customer.get('birthday','2002 06 03'))  #you can access not item in dictionries using get method
customer['name']='Sahan Avintha'  #update item in cutomer

#translare digit to letter

numbers={
    '0':'zero',
    '1':'one',
    '2':'two',
    '3':'three',
    '4':'four',
    '5':'five',
    '6':'six','7':'seven','8':'eight','9':'nine'
}
output=''
phone = input("Enter your phone number:")

for ch in phone:
    output += numbers[ch]+ " "
print(output)

#emojy converter
emojies = {
    'flower':'🌼',
    'star':'✨',
    'celebrate':'🥳',
    'red heart':'❤',
    'white heart':'🤍',
    'blue heart':'🩵',
    'cricket':'🏏',
    'happy':'😄'
}
words=input('>')

output=''
for i in words:
    output+=emojies.get(i,i)+' '
print(output)




