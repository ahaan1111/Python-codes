def odd_even(n):
    if n%2==0:
        print ("even")
    else:
        print ("odd")
print ("this number is", odd_even(3))

def collect (name,age):
    if age>=18:
        print ("adult")
    else:
        print ("kid")
print ("this person is",collect("jake",17))


def collect (word):
    count=0
    for i in word:
        if i== "a" or i=="e" or i=="i" or i=="o" or i== "u":
            count= count+1
    print ("number of vowels are",count)
collect ("thought")

            

        
    


