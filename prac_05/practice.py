# name_to_age = {"Bill": 21, "Jane":4, "Sven": 56}
# new_name = input("Enter the new name:")
# new_age = int(input("Enter the new age:"))
# name_to_age[new_name] = new_age
# for name,age in name_to_age.items():
#     print(f"{name:5} - {age:4}")
#
# words = ["aye", "bee", "sea", "bee"]
# words.remove("bee")
# print(words.pop())

"""ALl THE KEYS ARE STORED IN A LIST -- dict_keys([])"""
"""ITEM METHOD RETURN BOTH KEYS AND VALUES STORED IN NESTED TUPLES IN LIST"""

from operator import itemgetter

data = [['Derek',7],['Xavier',80],['Bob',612],['Chantanelle', 9]]
data.sort(key=itemgetter(1), reverse= True)
name_width = max(len(datum[0]) for datum in data)
score_width = max(len(str(datum[1])) for datum in data)
for datum in data:
    print(f"{datum[0]:<{name_width}} = {datum[1]:>{score_width}}")

# for name, score in data:
#     print(f"{name:<{name_width}} = {score:>{score_width}}")


name_to_age = {"Jame":21, "Bob":34, "Sven":56}

print("".join(f"{name} is {name_to_age[name]}\n" for name in name_to_age))


words_to_count = {"Apple":9, "Kiwi":10}
words = ["Apple","Orange"]
"""LBYP"""
for word in words:
    if word in words_to_count:
        words_to_count[word] += 1
        print(word, words_to_count[word])
    else:
        words_to_count[word] = 1
        print(word, words_to_count[word])

"""EASP"""
for word in words:
    try:
        words_to_count[word] += 1
        print(word, words_to_count[word])
    except KeyError:
        words_to_count[word] = 1
        print(word, words_to_count[word])

"""Get method"""
for word in words:
    words_to_count[word] = words_to_count.get(word, 0) + 1

module_to_number = {'CP1401':45, "CP1402":89, "CP2403":56}
modules = ['CP1401','CP5469','CP2403']
# for module in modules:
#     if module in module_to_number:
#         module_to_number[module] += 1
#         print(module, module_to_number[module])
#     else:
#         module_to_number[module] = 1
#         print(module, module_to_number[module])

for module in modules:
    module_to_number[module] = module_to_number.get(module,0) + 1
    print(module, module_to_number[module])

"""SET POP FIFO"""
set_example = set()
set_example.add('New')
print(set_example)

set_example.add(True)
print(set_example)

set_example.add(1)
print(set_example)

set_example.add(25)
print(set_example)

print(set_example.pop())
print(set_example)

example_1 = set_example.copy()
print(example_1)

print(example_1.pop())

set_example.clear()
print(set_example)

"""| Union - Difference & Interception ^ Symmetric Difference"""

name_to_age = {'Lea':45, "Eve":67}
print({name:age *2 for (name, age) in name_to_age.items() if age == max(name_to_age.values())})

flowers = ('cala lily', 'rose','rose','tulip')
numbers = {34, 56, 12, 90}
print(dict(zip(flowers, numbers)))
print(list(zip(flowers, numbers)))
print(tuple(zip(flowers, numbers)))
print(set(zip(flowers, numbers)))


"""Reading JSON"""
import json
name_to_age = {"Lea":45, "Eve":78}
json_name_to_age = json.dumps(name_to_age)
python_name_to_age = json.loads(json_name_to_age)


data = {'Derek':7,'Xavier':80,'Bob':612,'Chantanelle': 9}
# data.sort(key=itemgetter(1),reversed=True)
name_width = max(len(name) for name in data.keys())
score_width = max(len(str(score)) for score in data.values())
for name, score in sorted(data.items(), key=itemgetter(1), reverse=True):
    print(f"{name:<{name_width}} = {score:>{score_width}}")


strings = ['Name','Naing','Louis','Chantanelle','Flower']
# lengths_of_string = [len(string) for string in strings]
# def convert_list_to_dict(list1,list2):
#     """"Combine two lists into a dictionary"""
#     dict_of_lists = dict(zip(list1, list2))
#     return dict_of_lists
# print(convert_list_to_dict(strings, lengths_of_string))

def conver_list_to_dict(strings):
    """Convert list into dictionary"""
    # string_to_length = {name:len(name) for name in strings}
    # return string_to_length

    return {string:len(string) for string in strings}

print(conver_list_to_dict(strings))