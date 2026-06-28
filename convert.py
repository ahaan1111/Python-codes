import math

def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary_digits = []
    while n > 0:
        remainder = n % 2
        binary_digits.append(str(remainder))
        n = n // 2
    return "".join(binary_digits[::-1])

try:
    
    user_input = float(input("Enter a decimal number: "))
  
    whole_num = round(user_input)
    result = decimal_to_binary(whole_num)

    print(f"Whole number used: {whole_num}")
    print(f"Binary: {result}")

except ValueError:
    print("Please enter a valid number.")
