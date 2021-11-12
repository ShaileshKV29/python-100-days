import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# nr_characters = nr_letters - nr_symbols - nr_numbers
# password = ""

# for j in range(0, nr_letters):
#     random_letter = random.randint(0, len(letters) - 1)
#     password += letters[random_letter]

# for s in range(0, nr_symbols):
#     random_symbol = random.randint(0, len(symbols) - 1)
#     password += symbols[random_symbol]

# for n in range(0, nr_numbers):
#     random_number = random.randint(0, len(numbers) - 1)
#     password += numbers[random_number]

# print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = ""

for j in range(0, nr_letters):
    random_letter = random.randint(0, len(letters) - 1)
    password += letters[random_letter]

for s in range(0, nr_symbols):
    random_symbol = random.randint(0, len(symbols) - 1)
    password += symbols[random_symbol]

for n in range(0, nr_numbers):
    random_number = random.randint(0, len(numbers) - 1)
    password += numbers[random_number]

password = list(password)
p_len = len(password)

for i in range(0, p_len):
    random_index = random.randint(0, p_len - 1)
    password[i], password[random_index] = password[random_index], password[i]

new_password = ""
for z in range(0, p_len):
    new_password += password[z]

print(f"Your password is : {new_password}")


