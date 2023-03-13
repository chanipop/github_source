# param_example
def test(a, b=10, c=100):
    print(a+b+c)

#1 기본
test(10, 20, 30)
print()

#2 매개변수로 모두 지정
test(a=10, b=100, c=200)
print()

#3 매개변수로 불규칙하게 지정
test(c=1400, a=2222, b=300)
print()

#4 일부 지정 => 지정 안 된 매개 변수부터 할당 나머지는 디폴트로
test(10, c=200)
print()