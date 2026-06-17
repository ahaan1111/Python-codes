print (" select your ride")
print ("1= bike")
print ("2=car")
choice=int( input ("enter 1 or 2"))
if choice==1:
    print ("what kind of bike do you want?")
    print ("1= scootie")
    print ("2= scooter")
    choice2= int(input("choose your type of bike"))
    if choice2==1:
        print ("you chose scootie")
    else: 
        print ("you choose scooter")
if choice==2:
    print ("what kind of car?")
    print ("1= sedan")
    print ("2= SUV ")
    choice3= int(input("choose your type of car"))
    if choice3==1:
        print ("you choose sedan")
    else:
        print (" you choose SUV")