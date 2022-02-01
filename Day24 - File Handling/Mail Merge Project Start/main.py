starting_letter = open('Day24 - File Handling/Mail Merge Project/Input/Letters/starting_letter.txt')
old_letter = starting_letter.read()
names_file = open('Day24 - File Handling/Mail Merge Project/Input/Names/invited_names.txt')

names = names_file.readlines()
for name in names:
    output_file = open(f'Day24 - File Handling/Mail Merge Project/Output/ReadyToSend/send-to-{name[:-1]}.txt', "w")
    new_message = old_letter.replace("[name]", f"{name[:-1]}")
    output_file.write(new_message)
    output_file.close()


starting_letter.close()
names_file.close()

    