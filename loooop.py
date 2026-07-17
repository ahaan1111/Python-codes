i= 0
for i in range (2,6):
    for j in range (1, 13):
        print ( i,"*",j,"=", i*j )

i=0
for i in range (1,6):
    for j in range (0, i):
        print (i,end= " ")
    print ()