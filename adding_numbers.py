print(" -------- Adding Numbers -------- ")
print("\n")

# require user to input two numbers
user_input = input("Type any two numbers you would like to sum: ")

# these numbers are stored as strings and should be converted to integers
first_number = int(user_input[0])
second_number = int(user_input[1])

# sum the converted inputs
add_input = first_number + second_number


print(f"\nThe sum of your numbers are: {add_input}")
