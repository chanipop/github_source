#While value_delete
list_test = [1,2,1,2,1,2,1,2,3,2,4,1,23,]
value = 2

while value in list_test:
    list_test.remove(value)

print(list_test)