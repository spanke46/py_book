#5.8
list_users = ["admin","Erl","root","ted"]
for users in list_users:
    if users=="admin":
        print("Hello admin , would you like to see a status report?")
    else:
        print("Hello " + users + ", thank you for logging in again")
