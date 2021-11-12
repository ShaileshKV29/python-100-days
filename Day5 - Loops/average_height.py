students_heights = input("Enter the heights of the students : ").split()

for n in range(0 , len(students_heights)):
    students_heights[n] = int(students_heights[n])

# print(students_heights)
total = 0
index = 0
for i in students_heights:
    total += i
    index += 1

average = round(total/index)
print(average)

