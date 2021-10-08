# with open("weather_data.csv", "r") as content:
#     data = content.readlines()
#     print(data)

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         temp = row[1]
#         if temp != 'temp':
#             temperatures.append(int(temp))
#
# print(temperatures)

import pandas
# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data['temp']))
#
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data['temp'].to_list
# print(temp_list)
#
# # average = sum(temp_list) / len(temp_list)
# # print(average)
#
# average = data['temp'].mean()
# print(average)
# print(data["temp"].mean()
#
# maximun = data['temp'].max()
# print(maximun)

# get data in columns
# print(data['temp'])
# print(data.temp)
# print(data['condition'])
# print(data.condition)

# get data in row
# print(data[data.day == 'Monday'])
# maximun = data['temp'].max()
# print(data[data.temp == maximun])

# monday = data[data.day == "Monday"]
# print(monday.condition)

# create data frame from scratch
# data_dict ={
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

data = pandas.read_csv("Central_Park_Squirrel_Census.csv")
gray = sum(data['Primary Fur Color'] == 'Gray')
cinnamon = sum(data['Primary Fur Color'] == 'Cinnamon')
black = sum(data['Primary Fur Color'] == 'Black')

data_dict = {
    'SquirrelColor': ['Gray', 'Cinnamon', 'Black'],
    'CountSquirrel': [gray, cinnamon, black]
}

new_data = pandas.DataFrame(data_dict)
print(new_data)
new_data.to_csv('squirrel_count.csv')