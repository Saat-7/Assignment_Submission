dict={'Alice':88,'Tom':97,'Tim':80}
a=input("Enter student's name: ")
if a in dict.keys():
    print(f"{a}'s marks: ",dict[a])
else:
    print('Student not found')



