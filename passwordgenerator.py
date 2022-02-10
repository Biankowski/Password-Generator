# Password Generator
import random

print("")

# Basic ASCII art - https://fsymbols.com/text-art/
print("""\
██████╗░░█████╗░░██████╗░██████╗░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░
██╔══██╗██╔══██╗██╔════╝██╔════╝░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗
██████╔╝███████║╚█████╗░╚█████╗░░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║
██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗░░████╔═████║░██║░░██║██╔══██╗██║░░██║
██║░░░░░██║░░██║██████╔╝██████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝
╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░

░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░
██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝
██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗
╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║
░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝""")

print("")


# Function to generate weak passwords.
def weak_password():
    # Dictionary contaning all the numbers and characters that will be used to generate a password. Since we won't be making any math with these numbers, we can store them as a string. 
    word_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y' ,'Z', '!', '@', '#', '$', '%', '&', '{', '}', '[', ']']
    password = ""

    # This loop will go through all the itens in our "word_list" variable and, for each iteration, will add a random item to the empty "password" string. This loop will break after our string contains 6 characters.
    for i in word_list:
        password += random.choice(word_list)
        if len(password) > 5:
            break
    print(password)
    print("")

# Function to generate medium passwords.
def medium_password():
    # Dictionary contaning all the numbers and characters that will be used to generate a password. Since we won't be making any math with these numbers, we can store them as a string.
    word_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y' ,'Z', '!', '@', '#', '$', '%', '&', '{', '}', '[', ']'] 
    password = ""

    # This loop will go through all the itens in our "word_list" variable and, for each iteration, will add a random item to the empty "password" string. This loop will break after our string contains 12 characters.
    for i in word_list:
        password += random.choice(word_list)
        if len(password) > 13:
            break
    print(password)
    print("")

# Function to generate strong passwords.    
def strong_password():
    # Dictionary contaning all the numbers and characters that will be used to generate a password. Since we won't be making any math with these numbers, we can store them as a string.
    word_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y' ,'Z', '!', '@', '#', '$', '%', '&', '{', '}', '[', ']']
    password = ""

    # This loop will go through all the itens in our "word_list" variable and, for each iteration, will add a random item to the empty "password" string. This loop will break after our string contains 18 characters.
    for i in word_list:
        password += random.choice(word_list)
        if len(password) > 17:
            break
    print(password)
    print("")    

# Prompt the user to get the password length
choice = input("Type the number of characters you want your password to have: 6 caracters(weak), 12 caracters(medium), 18 caracters(strong): ")
print("")

if choice == '6':
    weak_password()
elif choice == '12':
    medium_password()
elif choice == '18':
    strong_password()
else:
    print("Something went wrong.")
