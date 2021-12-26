multiple_list = []

for i in range(100, 1000):
    if(i%3 == 0):
        multiple_list.append(i)

sum = sum(multiple_list)
count = len(multiple_list)
print(sum)
# print(count)
print(multiple_list)
print("\n\n")
for item in multiple_list:
    if(list(str(item)) != list(set(str(item)))):
        multiple_list.remove(item)

print(multiple_list)

if(sum%9 == 0):
    print("Divisible by 9")

if(sum%74 == 0):
    print("Divisible by 74")