
list_vocation = []
active = True
while active:
    questions= input('Where do you want to go vacation?')
    if questions == 'q':
        active=False
    list_vocation.append(questions)
print("Your list vacation:")
list_vocation.remove('q')
for sort_list in list_vocation:
    print(sort_list.title())

