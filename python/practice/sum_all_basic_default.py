# sum_all_basic_default
def sum_all(start = 0, end = 100, step=1):
    output = 0
    for i in range(start, end + 1, step):
        output += 1
    return output

# call function case

print("A. ", sum_all(0, 100, 10))
print("B. ", sum_all(end=200))
print("C. ", sum_all(end=300, step=2))