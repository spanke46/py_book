
#9.1
class Restaurant():
    def  __init__ (self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.door = 'ав'
    def describe_restaurant(self):
        print("Добро пожаловать в наш ресторан  " + self.restaurant_name + " " + self.cuisine_type + " кухни"  )

    def open_restaurant(self, s_door):
        self.door = s_door
        print('Ресторан ' + s_door)




my_rest = Restaurant('Яхта', 'Европйской')
my_rest2 = Restaurant('Моль', 'Итальянской')
my_rest3 = Restaurant('Ахер', 'Узбекской')

my_rest.describe_restaurant()
my_rest2.describe_restaurant()
my_rest3.describe_restaurant()



