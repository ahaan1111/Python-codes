user_num_str = input("Enter a number: ")
digit_count = 0

for char in user_num_str:
    if char.isdigit():
        digit_count += 1

print(f"The number {user_num_str} has {digit_count} digits.")