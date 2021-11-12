name1 = input("What is your name: ")
name2 = input("What is their name: ")

name_list = list(str.lower(name1)) + list(str.lower(name2))

print(name_list)

word1 = name_list.count("t") + name_list.count("r") + name_list.count("u") + name_list.count("e") 

word2 = name_list.count("l") + name_list.count("o") + name_list.count("v") + name_list.count("e") 

l_percentage = int(str(word1) + str(word2))


if l_percentage < 10 or l_percentage > 90:
    print(f"Your score is {l_percentage}, you go together like coke and mentos")
elif l_percentage > 40 and l_percentage < 50:
    print(f"Your socre is {l_percentage}, you are alright together")
else:
    print(f"Your score is {l_percentage}")