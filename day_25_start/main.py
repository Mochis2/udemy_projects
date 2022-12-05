# with open('./weather_data.csv') as file:
#     list_of_data = file.readlines()
# print(list_of_data)

# import csv

# with open('./weather_data.csv') as file:
#     data = csv.reader(file)
#     temperatures_list = []
#     for r in data:
#         if r[1] != 'temp':
#             temperatures_list.append(int(r[1]))
# print(temperatures_list)


# data = pandas.read_csv('./weather_data.csv')
# print(type(data))
# print(data['temp'])

# data_dict = data.to_dict()
# print(data_dict)

# avg_data = data['temp'].mean()
# max_data = data['temp'].max()

# Get column
# data.temp

# # get row
# data[data.day == 'Monday']

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == 'Monday']
# monday_fahrenheit = (monday.temp * 9/5) + 32
# # print(monday_fahrenheit)

# create dataframe from scratch
# data_dict = {
#     'students': ['Amy', 'James', 'Angela'],
#     'scores': [76, 56, 65]
# }
# new_data = pandas.DataFrame(data_dict)
# print(new_data)
# new_data.to_csv('./new_data.csv')

import pandas

data_squirrels = pandas.read_csv('./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

squirrels_colors = data_squirrels['Primary Fur Color']

squirrels_colors_gray = len(data_squirrels[squirrels_colors == 'Gray'])
squirrels_colors_cinnamon = len(data_squirrels[squirrels_colors == 'Cinnamon'])
squirrels_colors_black = len(data_squirrels[squirrels_colors == 'Black'])

squirrels_colors_dict = {
    'Fur Color': ['grey', 'red', 'black'],
    'Count': [squirrels_colors_gray, squirrels_colors_cinnamon, squirrels_colors_black]
}
new_data = pandas.DataFrame(squirrels_colors_dict)
new_data.to_csv('./squirrel_count.csv')
# primary fur color
# Gray
# Cinnamon
# Black
