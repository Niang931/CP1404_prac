in_file = open('new.txt','r')
for line in in_file:
    if line.startswith('F'):
        print(line)
in_file.close()