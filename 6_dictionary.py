'''#6.1
human_0 = {
    'first_name': 'igor',
    'last_name': 'titor',
    'age': 27,
    'city': 'Odessa'
    }
print(human_0['first_name'])
print(human_0['last_name'])
print(human_0['age'])
print(human_0['city'])
'''

"""human_0 = {
    'Igor': 'Python',
    'Lina': 'C#',
    'Vicky': 'Java',
    'Pasha': 'C++'
    }
for name, language in human_0.items():
    print(name.title() + "'s favorite language is " + language.title())
"""

human_0 = {
    'Igor': 'Python',
    'Lina': 'C#',
    'Vicky': 'Java',
    'Pasha': 'C++',
    'Lida': 'C++',
    'tolik': 'Java'
    }
for language in set (human_0.values()):
    print(language.title())