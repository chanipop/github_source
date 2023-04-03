# 1 to 10000
limit = 10000
i = 1
j = 0

while i < 10000:
    i += j
    if i == 1:
        j=2
    else:
        j += 1
print(f"{j - 1}를 더할 때 {limit}을 넘으며 그때의 값은 {i} 입니다.")