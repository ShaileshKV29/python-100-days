#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

starting_letter = open('Day24 - File Handling/Mail Merge Project/Input/Letters/starting_letter.txt')
old_letter = starting_letter.read()
names_file = open('Day24 - File Handling/Mail Merge Project/Input/Names/invited_names.txt')

names = names_file.readlines()
for name in names:
    output_file = open(f'Day24 - File Handling/Mail Merge Project/Output/ReadyToSend/send-to-{name[:-1]}.txt', "w")
    # print(name[:-1])
    new_message = old_letter.replace("[name]", f"{name[:-1]}")
    output_file.write(new_message)


output_file.close()
starting_letter.close()
names_file.close()

    