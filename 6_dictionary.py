#6.1

users = {
    'user_1' : {
        'first_name' : 'igor',
        'second_name' : 'titor',
        'age' : 25,
        'city' : 'odessa'
        },

    'user_2' : {
        'first_name' : 'pasha',
        'second_name' : 'oslo',
        'age' : 33,
        'city' : 'Lviv'
        },
    'user_3' : {
        'first_name' : 'oled',
        'second_name' : 'kislov',
        'age' : 44,
        'city' : 'Nikolaev'
        },
}
for username, user_info in users.items():
    print("№: " + username)
    full_name = user_info['first_name'] +" "+ user_info['second_name'] + ". Age " + str(user_info['age'])
    loc = user_info['city']
    print("\tFull name: " + full_name.title())
    print("\tCity: " +loc.title())

