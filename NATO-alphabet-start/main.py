student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
data = pandas.read_csv('./nato_phonetic_alphabet.csv')
phonetic_alaphabet_dict = {row.letter:row.code for (index, row) in data.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def handle_numbers():
    input_word = input('Enter a word: ').upper()
    try:
        list_input = [phonetic_alaphabet_dict[letter] for letter in input_word]
        
    except KeyError:
        print("What the fuck about 'phonetic' do you not understand??")
        handle_numbers()
        
    else:
        print(list_input)

handle_numbers()