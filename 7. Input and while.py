

'''# 7-4 Дополнения для пиццы
while True:
    m=input("Enter is topping name: ")
    print("Your are topping "+ m + " add!")
    if m == 'q':
        print("Exit")
        break
'''

'''#7-5. Билеты в кино

while True:
    age=int(input("Enter your age: "))
    if age < 3 :
        print("Your ticket is free")
    elif age ==3 or age <= 11:
        print("Cost ticket 10$")
    elif age > 12:
        print("Cost ticket 15$")
        break
'''

#7.6. Три выхода

while True:
    age=input("Enter your age: ")
    if age == 'q':
        print("Exit")
        break
    age = int(age)
    if age < 3 :
        print("Your ticket is free")
    elif age ==3 or age <= 11:
        print("Cost ticket 10$")
    elif age >= 12:
        print("Cost ticket 15$")

