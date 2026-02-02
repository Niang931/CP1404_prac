# filename = input("Enter file name:")
# in_file = open(filename, 'r')
# for line in in_file:
#     if line.startswith('#'):
#         print(line.strip())
# in_file.close()

s = "\tPython, Monty \n"
print(s[1], ".", sep='')

print(s.strip(), '.', sep='')

s.replace(' ','*')
#doesn't get rid of tab space, only one space around the Monty

print(s.lstrip(), '.',sep='')
#strip the left space. l = left. tab space will be removed

print(s.strip().split(','))

# name = input('name:')
# with open('name.txt', 'w') as out_file:
#     print(name, file=out_file)
# print('done')

EXTENSION = '.txt'
files = ['Bob', 'Naing', 'Elias', 'Lily']
# for index, file in enumerate(files):
#     with open(f'{file}{EXTENSION}', 'w') as out_file:
#         print(index+1, file, file=out_file)

# for i in range(len(files)):
#     with open(f'{files[i]}{EXTENSION}', 'w') as out_file:
#         print(i+1, files[i], file=out_file)
#         out_file.write(str(i+1))

# in_file = open('name.txt','r')
# lines = in_file.readlines()
# i = 0
# while i < len(lines) - 1:
#     name = lines[i].strip()
#     age = lines[i+1].strip()
#     try:
#         age = int(age)
#         print(f'{name} is {age} years old')
#
#     except ValueError:
#         pass
#     i += 2
#
# in_file.close()

in_file = open('name.txt','r')
lines = in_file.readlines()
for i in range(0,len(lines),2):
    name = lines[i].strip()
    age = lines[i+1].strip()
    try:
        age = int(age)
        print(f"{name} is {age} years old")
    except ValueError:
        pass
in_file.close()









