# for loop in list (list comprehensions)
array = [i * i for i in range(0, 20, 2)]

print(array)
print()

# condition
array_2 = [j * j for j in range(0, 20, 2) if j * j < 100]
print(array_2) 