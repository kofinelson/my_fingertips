# importing relevant modules
import random

print(""" --------- Random Password Generator --------- """)
print("\n")

# listing the characters for the password
pass_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789`~!@#$%^&*()-_+=[{]}|\?/.><,"

# length of password. The user would have to choose a string of 8 characters or more
len_of_password = int(
    input("What would you like to be the length of your password? "))

# number of passwords the user would like to generate
num_of_passwords = int(input("How many passwords would like to generate? "))

print('\nhere are your passwords: ')

for pswd in range(num_of_passwords):
    passwords = ""
    for c in range(len_of_password):
        passwords += random.choice(pass_characters)
    print(passwords)
