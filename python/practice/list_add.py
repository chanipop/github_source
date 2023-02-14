# 리스트 선언
list_a = [1, 2, 3]

# 리스트 뒤에 요소 추가
print("# 리스트 뒤에 요소 추가하기")
list_a.append(4)
list_a.append(5)
print(list_a)
print()

# 리스트 중간에 요소 추가 / 배열의 위치에 값을 추가하고 뒤로 밀어냄
list_a.insert(0, 10)
print(list_a)


# 리스트 확장
list_a.extend([6, 7, 8])
print(list_a)

list_a.append(10)
print(list_a)