def add (P, Q):
    return P + Q
def subtract (P, Q):
    return P - Q
def multiply (P, Q):
    return P * Q
def divide (P, Q):
    return P / Q
print ("please select option")
print ("a. add")
print ("b. subtract")
print ("c. multiply")
print ("d. divide")
choice= input ("please enter your choice")
num1= int (input("enter first number"))
num2= int (input("enter second number"))
if choice== "a": 
    print ("result is ", add(num1, num2))
elif choice== "b": 
    print ("result is ", subtract(num1, num2))
elif choice== "c": 
    print ("result is ", multiply(num1, num2))
elif choice== "d": 
    print ("result is ", divide(num1, num2))
else:
    print ("wrong choice")
