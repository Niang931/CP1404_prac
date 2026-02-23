from operator import itemgetter

data = [['Lea',34], ['Sam',24],['Eve',67]]
data.sort()
print(data)
data.sort(key=itemgetter(1))
print(data)
data.sort(key=itemgetter(1), reverse=True)
print(data)

words = 'This is Python'
words = words.split()
print(words)

#list comprehension
words = [word for word in words]
print(words)

print([word for word in words if len(word) > 2])

# words = [len(word) for word in words]
# print(words)

print([word.upper() for word in words])

# numbers = [23, 57, 45, 23]
# numbers = [number*2 for number in numbers if number > 20]
# print(numbers)

cars = [['Audi', 2006],['BMV',2016],['Jaguar', 2026]]
print([tuple(car) for car in cars])
print([car[0] for car in cars])
print([car[1] * 2 for car in cars])
print(min(car[1] for car in cars))

"""Only two lists with the assignment '=' would be the same.
Even when two lists are of the same value, without '=' they are not the same
"""
# numbers = [23,45,67,78]
# new_numbers = numbers
# print(new_numbers)
# new_numbers.append(90)
# print(numbers)
# print(numbers == new_numbers)
# numbers_test = [23,45,67,78,90]
# print(numbers == numbers_test)
# print(numbers is numbers_test)


print([x+y for x in range(1,4) for y in range(1,4)])
# function (x+y) outer for loop nested for loop

names = ['Ada','Alan','Bill','John']
print(",".join(names))
name_to_remove = input("WHo do you want ot remove:")
while name_to_remove != "":
    try:
        names.remove(name_to_remove)

    except ValueError:
        print("Name is not ont the list")
    print(names)
    name_to_remove = input("WHo do you want ot remove:")

"""with open () as in_file:
        list = in_file.readlines()
    for item in list:
        pass
"""
#Do not include processing within the with statement
#Store FILENAME not just 'file.txt'

from operator import itemgetter
data = [['Derek', 7], ['Xavier', 80], ['Bob', 612], ['Chantanelle', 9],['Lowaiusdfhiasdc',23405]]
name_format = max(len(datum[0]) for datum in data)
number_format = max(len(str(datum[1])) for datum in data)
data.sort(key=itemgetter(1), reverse=True)
for datum in data:
    print(f"{datum[0]:<{name_format}} = {datum[1]:>{number_format}}")

things = [True, 1,2, 'Good', [1,10]]

values = [[3,4,5,1],[33,6,1,2]]
v = values[0][0]
for row in range(0, len(values)):
    for column in range(0, len(values[row])):
        if v < values[row][column]:
            v = values[row][column]
print(v)

def main():
    numbers = get_number()
    square_numbers(numbers)
    display_numbers(numbers)

def get_number():
    input_numbers = input("Enter number:")
    cleaned_numbers = input_numbers.split(',')
    return cleaned_numbers

def square_numbers(numbers):
    # new_numbers = []
    # for number in numbers:
    #     new_number = float(number) ** 2
    #     new_numbers.append(new_number)
    # return new_numbers
    for i in range(len(numbers)):
        numbers[i] = float(numbers[i]) ** 2


def display_numbers(numbers):
    numbers.sort()
    print("..".join(str(number) for number in numbers))
    # for number in numbers:
    #     print(number, end='.')

main()

