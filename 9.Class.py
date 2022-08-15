
#9.3

class User():
    def __init__(self, first_name, last_name, city,):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.login_attempts = 0
    def describe_user(self):
        print(f"Основная информация: {self.first_name}  {self.last_name}  {self.city}")

    def greet_user(self):
        print(f"Привет  {self.first_name}  {self.last_name}")


    def  increment_login_attempts(self, attempts=1):
        self.login_attempts += attempts

    def  reset_login_attempts(self,res_attempts=1):
        self.login_attempts -= res_attempts

user_1 = User('igor', 'titor', 'odessa')
user_2 = User('lina', 'ostin', 'kiev')

user_1.describe_user()
user_1.greet_user()

user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.reset_login_attempts()

print(user_1.login_attempts)



