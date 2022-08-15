
#9.3

class User():
    def __init__(self, first_name, last_name, city):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
    def describe_user(self):
        print(f"Основная информация: {self.first_name}  {self.last_name}  {self.city}")

    def greet_user(self):
        print(f"Привет  {self.first_name}  {self.last_name}")
user_1 = User('igor', 'titor', 'odessa')
user_2 = User('lina', 'ostin', 'kiev')

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()


