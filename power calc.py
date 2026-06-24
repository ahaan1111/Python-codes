base_num_str = input("Enter the base number: ")
base_number = float(base_num_str) # Convert to a number

exponent_str = input("Enter the power (exponent): ")
exponent = float(exponent_str) # Convert to a number

result = base_number ** exponent # Calculate base raised to the power of exponent

print(f"{base_number} raised to the power of {exponent} is: {result}")