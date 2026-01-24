"""
get number of gifts
get number of students
gifts per student = number of gifts // number of students
gifts remained = number of gifts % number of students
display gifts per student, gift remained
"""
# number_of_gifts = int(input("Number of gifts:"))
# number_of_students = int(input("Number of students:"))
# gifts_per_student = number_of_gifts // number_of_students
# gifts_remained = number_of_gifts % number_of_students
# print(gifts_per_student)
# print(gifts_remained)

# TAX_RATE = 0.09
# item_price = float(input("Item price:$"))
# is_taxed = input("Does it have GST? (y/n):").lower()
# if is_taxed == 'y':
#     item_price = item_price - (item_price * TAX_RATE)
# print(f"${item_price:.2f}")

# index = 1
# number = int(input("Enter number:"))
# for i in range (1, number+1):
#     print(i, end="")
# print()
#
# while index < number + 1:
#     print(index, end="")
#     index += 1

# SECRET_NUMBER = 4
# guess = int(input("Guess:"))
# while guess != SECRET_NUMBER:
#     guess = int(input("Guess:"))
# print(f"Yes! The number is {SECRET_NUMBER}")

user_name = input("Name:").upper()
while user_name == "":
    user_name = input("Name:").upper()
salary = float(input("Salary:$"))
while salary < 0 :
    salary = float(input("Salary:$"))
print(user_name)
print(f"${salary:.2f}")
