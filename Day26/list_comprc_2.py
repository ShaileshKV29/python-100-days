names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

new_names = [name.upper() for name in names if len(name) >= 5]
print(new_names)

numbers = [1,2,3,4,5,6,7,8,9]

new_numbers = [n for n in numbers if n%2==0]
print(new_numbers)