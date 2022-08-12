



#10.4
def count_words(file_path):
    try:
        with open(file_path, encoding='utf-8') as f_write:
            content = f_write.read()
            word = content.split()
            num_words = len(word)
            print(num_words)
    except FileNotFoundError:
        print('File not found')

file_path = input('Enter path: ')
count_words(file_path)
