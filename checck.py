a= int (input("enter your first number"))
b= int (input("enter your 2nd number"))
if (a%b==0):
    print (" no remainder")
else: 
    print (" reaminder")


abcd= int (input("enter your marks"))
if abcd>= 90:
    print ("A")
elif abcd>= 80 and abcd < 90:
    print ("B")
elif abcd>= 70 and abcd < 80:
        print ("C")
else: 
        print ("D, try again")


x= int (input("enter your number to factorialize"))
product= 1
i=1
for i in range(1, x+1):
    product= product*i
print ("the factorial is",product)


z= int (input("enter your number to add up to"))
sum=0
i=1
for i in range(1, z+1):
    sum= sum+i
print ("the sum is",sum)



y= int (input("enter your number to square up to"))
product= 1
i=1
for i in range(1, y):
     sq= i*i
     print ("the answer is", sq)