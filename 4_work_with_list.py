#Копия списка
my_food = ['pizza', 'burger', 'cake', 'bread', 'sup']
friend_food = my_food[:]
for my_favorite in my_food:
    print('This favorite my food ' + f'{my_favorite}')
friend_food.append('salad')
for friend_favorit_food in friend_food:
    print('This favorite food my friends ' + f'{friend_favorit_food}')
