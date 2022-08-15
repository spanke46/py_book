



#10.4
file_path = 'c:\py\guest.txt'

while True:
    name= input('Enter your name: ')
    if name == 'q':
        print('Exit')
        break
    else:
        with open(file_path, 'a') as f_write:
            print("Hello " + name)
            f_write.write(name + '\n')

