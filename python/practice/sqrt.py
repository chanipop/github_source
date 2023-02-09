import math

input_row = input("밑변의 길이를 입력해주세요: ")
input_height = input("높이의 길이를 입력해주세요: ")

row = int(input_row)
height = int(input_height)

side = math.sqrt(row ** 2 + height **2)

print(f"= 빗변의 길이는 {side}입니다.")