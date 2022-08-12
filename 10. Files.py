



#10.4
file_path = 'c:\py\pi.txt'
with open(file_path, encoding='utf-8') as f_write:
    content = f_write.read()
word = content.split()
num_words = len(word)
print(num_words)
