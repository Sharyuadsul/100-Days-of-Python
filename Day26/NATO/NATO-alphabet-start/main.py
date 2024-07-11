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
{"A": "Alfa", "B": "Bravo"}
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

df = pandas.read_csv("nato_phonetic_alphabet.csv")
#print(df.to_dict()) not in required format
# print(df)

my_dict = {row["letter"]:row["code"] for (index,row) in df.iterrows()}
print(my_dict)

def generate_nato():
    word = input("Enter the Word: ").upper()
    try:
        result = [my_dict[item] for item in word]
    except KeyError:
        print("sorry..only letters please!")
        generate_nato()
    else:
        print(result)

generate_nato()