#1
username = input("Enter user name:")
out_file = open('name.txt','w')
print(username, file=out_file)
out_file.close()

#2
in_file = open('name.txt','r')
print(f"Hi, {in_file.read().strip()}")
in_file.close()

#3
with open('numbers.txt','r') as in_file_1:
    num1 = int(in_file_1.readline())
    num2 = int(in_file_1.readline())
print(num1 + num2)

#4
total = 0
with open('numbers.txt','r') as in_file:
    for line in in_file:
        number = int(line)
        total += number
print(total)

