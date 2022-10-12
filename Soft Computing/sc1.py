# set1 = input("Enter first Set: ")
# set2 = input("Enter second Set: ")

# set1 = set(set1.split())
# set2 = set(set2.split())

set1 = {1,2,3,4,5,6,7,8,9,10}
set2 = {1,2,3,44,55,62,27,81,91,98}

union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set1.difference(set2)

complement1 = union_set - set1
complement2 = union_set - set2

print(union_set)
print(intersection_set)
print(difference_set)
print(complement1)
print(complement2)