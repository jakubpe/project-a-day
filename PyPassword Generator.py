import random
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
            'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%',
           '(', '-', '"', '*', '|', ',', '&', '<', '`', '}',
           '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
letters = int(input("How many letters would you like?\n"))
digits = int(input("How many digits would you like?\n"))
signs = int(input("How many special signs would you like?\n"))
password = []
for char in range(0, letters):
    password.append(random.choice(alphabet))
for char in range(0, digits):
    password.append(random.choice(numbers))
for char in range(0, signs):
    password.append(random.choice(symbols))
random.shuffle(password)
pass_as_string = ''.join(password)
print("Your password is: " + pass_as_string)

