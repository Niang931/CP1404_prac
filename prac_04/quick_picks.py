import random
MIN_VALUE = 1
MAX_VALUE = 45
NUMBER_OF_RANDOM_VALUES = 6
number_of_lines = int(input("How many quick picks?:"))
for i in range(number_of_lines):
    for j in range(NUMBER_OF_RANDOM_VALUES):
        print(f"{random.randint(MIN_VALUE, MAX_VALUE+1):2}", end=" ")
    print()
