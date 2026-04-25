amount= int(input("enter the amount"))
note1= amount//100
note2= (amount%100)//50
note3= ((amount%100)%50)//20
note4= (((amount%100)%50)%20)//10
print ("amount of 100 dollars notes", note1 )
print ("amount of 50 dollars notes", note2 )
print ("amount of 20 dollars notes", note3 )
print ("amount of 10 dollars notes", note4 )
