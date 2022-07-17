'''Проверка равенства и неравенства строк
car= input('Enter name the car: ')
if car=='bmw':
    print('Yes')
else:
    print('no')
#Проверки с использованием функции lower().
name= input('Enter name: ')
if name.lower()=='lina':
    print('Yes')
else:
    print('no')

#Числовые проверки равенства
print('Check ==')
num_1 = input('Enter first number: ')
num_2 = input('Enter second number: ')
if num_1==num_2:
    print('Yes')
else:
    print('No')

#неравенства
print('Check !=')
num_1 = input('Enter first number: ')
num_2 = input('Enter second number: ')
if num_1!=num_2:
    print('Yes')
else:
    print('No')

#Проверки с ключевым словом and и or.
in_user = input('Enter your name: ')
in_pass = input('Enter your password: ')
user = 'igor'
passw = '123'
if in_user.lower() == user and in_pass == passw:
    print('Welcome to site')
else:
    print('Login or password is not correct' )

#Проверка вхождения элемента в список
in_guest= input('Enter your name: ')
guests = ['igor', 'pasha','masha']
if in_guest.lower() in guests:
    print('Welcome')
else:
    print('You are not in list' )
'''
#Проверка отсутствия элемента в списке.
ban_guests = ['igor', 'pasha','masha']
guest= input('Enter your name: ')
if guest.lower() not in ban_guests:
    print('Welcome')
else:
    print('You are banned' )