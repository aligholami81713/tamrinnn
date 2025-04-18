import random as R
file=open('numbers.txt','w') 
for i in range (100):
    number=R.randint(1,100)
    file.write(str(number)+('\n'))
file.close