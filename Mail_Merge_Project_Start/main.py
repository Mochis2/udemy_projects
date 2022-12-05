
#Append each name in file into new list without \n in the string
with open('./Input/Names/invited_names.txt') as names:
    name_file = names.readlines()

names_cleaned = []
for i in name_file:
    names_cleaned.append(i.replace("\n", ""))


#Open the letter template save it into a var as a string 
with open('./Input/Letters/starting_letter.txt') as letter:
    letter_text = letter.read()

#for each name in the list create new file with '[name] replaced with actual name
for name in names_cleaned:
    with open(f'./Output/test/{name}.txt', mode='x') as new_file:
        new_file.write(letter_text.replace('[name]', f'{name}'))

