with open('./file1.txt') as file1:
    list_of_numbers1 = file1.readlines()

with open('./file2.txt') as file2:
    list_of_numbers2 = file2.readlines()

list_of_numbers1 = [num.strip() for num in list_of_numbers1]
list_of_numbers2 = [num.strip() for num in list_of_numbers2]


result1 = [int(num) for num in list_of_numbers1 if num in list_of_numbers2]
print(result1)


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
list_sentence = sentence.split()
result2 = {word:len(word) for word in list_sentence}
print(result2)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:
weather_f = {day:(degree * 9/5) + 32 for (day, degree) in weather_c.items()}


print(weather_f) 
