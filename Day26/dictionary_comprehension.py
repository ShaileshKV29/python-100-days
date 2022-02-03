import random

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

new_dict = {name:random.randrange(1, 100) for name in names}
print(new_dict)

passed_students = {key:value for (key, value) in new_dict.items() if value >= 60}
print(passed_students)