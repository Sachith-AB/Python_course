#secret number game using while loop

print('You can choose one number is "1" to "6".If you choose correct number you win.You have only 3 chance to play.')

secret_num=5
i=3
while i>0:
    choose=input('Choose value:')
    if int(choose)==secret_num:
        print('You win...')
        i=-1
    else:
        if i>1:
            print('Try again')
            i=i-1 
        else :
            print('You Failed')
            break
        
   
        
        
       
    


