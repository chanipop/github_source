# #Giza pyramid
# for i in range(31, 1 - 1, -2):
#     # print(i)
#     a = i - 1
#     b = a / 2
#     output = ""
#     for i in range(0, i):
#         if i < b + 1:
#             output += " "
#         elseif 


n = 31
output = ""
print(f"pyramid's height is {n}m\n")

for i in range(1, n - 1, 2):
    a = int((n - i) / 2)
    output += " " * a + "*" * i + " " * a
    output += "\n"

print(output)