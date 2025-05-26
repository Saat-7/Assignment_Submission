readme=''
try:
    file1 = open('sample.txt', 'r')
    readme = file1.read()
    file1.close()
except FileNotFoundError:
    print('File \'sample.txt\' not found')
finally:
    print(readme)



