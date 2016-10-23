text = 'This is some text!!\n'

file = open('file.txt', 'a')
for each in range(10):
    file.write(text)

file.close()
