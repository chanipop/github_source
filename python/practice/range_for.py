# 범위 for
for i in range(5):
    print(str(i) + "=반복변수")

# for 리스트 범위
array = [273, 23, 123, 545, 33]

for element in array:
    print(element)

print()

for i in range(len(array)):
    print(f"{i}번쨰 반복 : {array[i]}")

# reverse
for i in range(4, 0 - 1, -1):
    print(f"현재 반복 변수 : {i}")

for i in reversed(range(5)):
    print(i)