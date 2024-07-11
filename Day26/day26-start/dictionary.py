# names= ["john", "carolina", "smith", "conner", "lily"]
# import random
#
# student_dict = {student:random.randint(1,100) for student in names}
# print(student_dict)
#
# passed_students = {key:value for (key,value) in student_dict.items() if value>=60}
# print(passed_students)


import pandas as pd

student = {
    "name": ["john", "carolina", "smith", "conner", "lily"],
    "scores": [23, 45, 78, 94, 43]
}

#looping through the dict
# for (key,value) in student.items():
#     print(key)
#     print(value)

df = pd.DataFrame(student)
print(df)

#looping through the df
# for (key,value) in df.items():
#     print(value)

for (index,row) in df.iterrows():
    # print(index)
    # print(row)
    #print(row["name"])
    if row["name"] == "john":
        print(row.scores)
