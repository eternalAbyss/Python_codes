# Beast PC check 
files = []
for i in range(100000):
    files.append(open('some_file.txt', 'r'))
    print(i)
print('You have a beast PC!')