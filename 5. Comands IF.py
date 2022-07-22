"""#5.8
list_users = ["admin","Erl","root","ted"]
for users in list_users:
    if users == "admin":
        print("Hello admin , would you like to see a status report?")
    else:
        print("Hello " + users + ", thank you for logging in again")
"""

"""#5.9
list_users = [""]
for users in list_users:
    if users == "":
        print("We need to find some users!")
"""
"""#5.10
current_users = ["lina","dima","denis","vera","geid"]
new_users = ["lina","dima","vasya","liza","pit"]
for users in new_users:
    if users in current_users:
        print("User " +users.title() + " already exists")
    else:
        print("Add new user " + users )
"""
#5.11 Порядковые числительные

numbers = list(range(1,10))
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(str(number)+"th")
