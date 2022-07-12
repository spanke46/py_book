
name = input('What is your name?')

names = ['vicky','igor','pasha','masha']
names.append(name)

for guest in names:
    print (f'Hello {guest.title()}, I glad to see you')
