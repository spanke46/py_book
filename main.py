


names = ['vicky','igor','pasha','masha']
for guest in names:
    print (f'Hello {guest.title()}, I glad to see you')
names.remove('pasha')
print("Pasha can't come")
print('New guest list')
for guest in names:
    print(guest.title())
print('I bought the new table. I invited more guests! ')
names.insert(0, 'Valera')
names.insert(2, 'Nikita')
names.append('Tolik')
print('New guest list')
for guest in names:
    print(guest.title())