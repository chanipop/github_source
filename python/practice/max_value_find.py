# max value find
max_value = 0
a = 0
b = 0

for i in range(1, 100):
    j = 100 - i
    a = i
    b = j

    if a == 1:
        c = 1
    else:
        c = a - 1

    if b == 99:
        d = 99
    else:
        d = b + 1

    before_value = c * d
    max_value = a * b

    if max_value 

print(max_value)
