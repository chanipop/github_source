#enumerate
list_a = ["요소1", "요소2", "요소3"]

print("# 단순출력")
print(list_a)
print()

# enumerate() 함수 적용 출력
print("# enumerate() 함수 적용 출력")
print(enumerate(list_a))
print()

# list 함수로 강제변환출력
print("# list 함수로 강제 변환 출력")
print(list(enumerate(list_a)))
print()

# for 반복문과 enumerate() 함수 조합 사용
print("# 반복문과 조합")
for i , value in enumerate(list_a):
    print(f"{i}번쨰 요소는 {value}입니다.")