input_half_circle = input("구의 반지름을 입력해주세요: ")
r = int(input_half_circle)
pi = 3.141592

dd = (4/3) * pi * (r**3)
ww = 4 * pi * (r**2)

print("= 구의 부피는 {}입니다.".format(dd))
print(f"= 구의 겉넓이는 {ww}입니다.")