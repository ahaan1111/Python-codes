medical=input("Do You have a medical cause?: Y/N" ).strip().upper()
if medical=="Y":
    print("you're allowed")
else: 
    attendance=int( input("enter % of attendance"))
    if attendance >=75:
        print ("you're allowed")
    else: 
     print ("You cant take the exam")