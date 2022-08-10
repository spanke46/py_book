
'''#8.3 . Вызовите функцию с использованием позиционных аргументов
# во второй раз с использованием именованных аргументов


def make_shirt(size, text):
    print(f"You have the shirt {size} size and this this text '{text}'")

make_shirt(53,'Hello')
make_shirt(text='Hello',size='53')
'''

'''#8-4

def make_shirt(size='L', text='I love Python'):
    print(f"You have the shirt {size} size and this this text '{text}'")


make_shirt(size='XL', text='Hello')
'''
#8-5

def describe_city(city='Odessa', text='is my favorine city'):
    print(f"{city} {text}")

describe_city()
describe_city(city='Kiev')
describe_city(city='Lviv')