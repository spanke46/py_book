





'''#8.3 Футболка
def make_shirt(size, text):
    print(f"Your shirt have got size {size}, and this text {text}")

#position argument
make_shirt(54, 'Hello')

#name argument
make_shirt(text='Hi there!',size=45 )
'''

'''#8.4 Большие футболки
def make_shirt(size="L", text="I love python"):
    print(f"Your shirt have got size {size}, and this text {text}")

make_shirt(text="I don't love python")
'''
def describe_city(city="Kyiv", county="Ukraine"):
    print(f"{city.title()} is in  {county.title()}")
describe_city()
describe_city(city="Odessa")
describe_city(city="Lviv")
describe_city("dnepr")



