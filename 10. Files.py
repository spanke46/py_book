

file_path = 'c:\py\pi.txt'

with open(file_path) as file_test:
    string = file_test.read()

print(string)

change = string.replace('Python', 'C#')
print(change)
