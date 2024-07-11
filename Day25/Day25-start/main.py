# with open("weather_data - Sheet1.csv") as data:
#     list = data.readlines()
#     print(list)

# import csv
#
# with open("weather_data - Sheet1.csv") as weather:
#     data = csv.reader(weather)
#     temp = []
#     for row in data:
#         if row[1] != "temp":
#             temp.append(int(row[1]))
#             print(temp)


import pandas as pd
df = pd.read_csv("weather_data - Sheet1.csv")
# print(df["temp"])
# print(type(df))
# print(type(df["temp"]))

# data_dict = df.to_dict()
# print(data_dict)
#
# temp_list = df["temp"].to_list()
# print(len(temp_list))
#
# avg = sum(temp_list)/len(temp_list)
# print(avg)
# # or
# print(df["temp"].mean())

# print(df["temp"].max())

#get the column data:
# print(df["condition"])
#  or
# print(df.condition)

#get the row data
# print(df[df.day == "Monday"])
# print(df[df.temp == df.temp.max()])
#
# monday = df[df.day == "Monday"]
# print(monday.condition)
# monday_temp = monday.temp
# monday_temp_f = monday_temp*9/5 + 32
# print(monday_temp_f)

#creating a dataframe
# my_dict = {
#     "students":["fvhgvh", "trwsefc", "rdersv"],
#     "marks": [34, 78, 43]
# }
# data = pd.DataFrame(data=my_dict)
# # print(data)
# data.to_csv("new_csv.csv")

df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240627.csv")
gray_squirrals = len((df[df['Primary Fur Color'] == "Gray"]))
red_squirrals = len((df[df['Primary Fur Color'] == "Cinnamon"]))
black_squirrals = len((df[df['Primary Fur Color'] == "Black"]))
print(gray_squirrals)
print(red_squirrals)
print(black_squirrals)

squirral_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [gray_squirrals, red_squirrals, black_squirrals]
}

data_squirrals = pd.DataFrame(data=squirral_dict)
# print(data_squirrals)
data_squirrals.to_csv("squirrals_dataset.csv")

