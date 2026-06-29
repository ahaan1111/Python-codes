print ("write pattern pyramid")
n= int (input("enter the number of stars"))
for i in range(n):
    for j in range(i + 1):
        print ("*",end= " " )
    print ()