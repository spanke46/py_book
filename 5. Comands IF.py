"""#Цвета 1-2
#выберите цвет, как это было сделано в упражнении 5-3, и напишите цепочку if-else.
#Если переменная содержит любое другое значение, выведите сообщение о том, что игрок только что заработал 10 очков.
color = input('Enter the name color: ')
alien_color = ["green", "yellow","red"]
if color.lower() in alien_color:
    print("Player gets five points")
else:
    print("Player doesn't  the points")
"""
"""#Цвета 3. преобразуйте цепочку if-else из упражнения 5-4 в цепочку if-elif-else.

color = input('Enter the name color: ')
if color.lower():
    print("Player gets 5 points")
elif color.lower() == "yellow":
    print("Player gets 10 points")
elif color.lower() == "red":
    print("Player gets 15 points")
else:
    print("Player doesn't  the points")
"""
#Периоды жизни
age = int(input("Enter age: "))
if age < 2:
    print("Baby")
elif age>= 2:
    print('babe')
elif age>=4:
    print("Kid")