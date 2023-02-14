# 리스트에서 제거하기
print("Method 1")
list_a = [1, 2, 3, 4, 5, 6]

del list_a[1]
print(list_a)
print("")

print("Method 2")
list_a.pop(0)
print(list_a)
print("")

print("Method 3")
list_a.remove(3)
print(list_a)
print("")

print("Method 4")
list_a.clear()
print(list_a)
print("")
