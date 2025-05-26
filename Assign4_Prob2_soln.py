a=input('Enter text to enter into file: ')
file1=open('output.txt','r+')
file1.truncate()
wr=file1.write(a+' ')
print('Data successfully written')
file1.close()
b=input('Enter data to append in the file: ')
file1=open('output.txt','a')
app=file1.write(b)
print("Data successfully appended")
file1.close()

file1=open('output.txt','r')
readme=file1.read()
print('Final contents of the files: ')
print(readme)
file1.close()



