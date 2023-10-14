from itertools import permutations, combinations

target = [1,2,3,4]
per = permutations(target, 2)
for i in per:
    print(i, end=" ")
print()


com = combinations(target, 2)
for i in com:
    print(i, end=" ")
print()