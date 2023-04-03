numbers = [1,2,3,1,4,1,5,3,5,7,4,3,7,4,3,2,1,2,3,6,7,8,9,6,4,3,4,5,7,8,4,3,2]
counter = {}

for number in numbers :
    counter[number] = 0
for number in numbers:
    counter[number] = counter[number] + 1

print(counter)