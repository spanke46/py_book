#Create list guests
names = ['Andrey','igor','pasha','masha']
#Create cycle 'for' for greetings guests. Use f string.
for guest in names:
    print (f'Hello {guest.title()}, I glad to see you')
# Del value in list
names.remove('pasha')
print("Pasha can't come")
print('New guest list')
for guest in names:
    print(guest.title())
print('I bought the new table. I invited more guests! ')
#Add inpun the name
input_name = input('Enter the new name ')
#Add the new name in list
names.append(input_name)
names.append('Tolik')
print('New guest list')
for guest in names:
    print((guest.title()))
#Add long a string
print('Number of guests ' + str(len(names)))
del_guest = names.pop()
del_guest = names.pop()
del_guest = names.pop()
print('On dinner invited only two guests, sorry')
#Add method sort
names.sort()
for guest in names:
    print((guest.title()))

print('Nubmer of guests ' + str(len(names)))
