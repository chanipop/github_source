# factorial_for
def factorial(n):
    output = 1

    for i in range(1, n + 1):
        output *= i
    return output

print("1! :", factorial(1))
print("2! :", factorial(2))
print("3! :", factorial(3))
print("12! :", factorial(12))