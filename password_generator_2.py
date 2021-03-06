# importing relevant modules
import random

print("""\n --------- Random Password Generator --------- """)
print("\n")

# listing the characters for the password
caps_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
small_chars = "abcdefghijklmnopqrstuvwxyz"
numbs = "0123456789"
spec_chars = "`~!@#$%^&*()-_+=[{]}|\?/.><,"

# length of password. The user would have to choose a string of 8 characters or more
len_of_password = int(
    input("What would you like to be the length of your password? "))

# number of passwords the user would like to generate
num_of_passwords = int(input("How many passwords would like to generate? "))

print('\nHere are your passwords: ')

# the password must have at least all the characters
for pswd in range(num_of_passwords):
    passwords = ""
    for c in range(len_of_password):
        if len_of_password < 8:
            print(f"Password cannot be less than 8 characters")

        passwords += random.choice(pass_characters)
    print(passwords)
