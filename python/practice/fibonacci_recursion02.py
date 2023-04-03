# fibonacci_recursion02
counter = 0

def fibonacci(n):
    print(f"fibonacci({n})를 구합니다.")
    global counter
    counter += 1        # 함수 내부에서 외부의 변수를 참조할 수 없으므로 global 키워드를 사용
    if n == 1 :
        return 1
    if n == 2 :
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print("fibonacci(15)", fibonacci(15))