#Dictionary

dictionary = {
    "name" : "7D 건조 망고",
    "type" : "당절임",
    "ingredient" : ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin" : "필리핀"
}

#출력
print("name : ", dictionary["name"])
print("type : ", dictionary["type"])
print("ingredient : ", dictionary["ingredient"])
print("origin : ", dictionary["origin"])
print()

# 값 변경
dictionary["name"] = "8D 건조 망고"
print(dictionary["name"])
print()

# 딕셔너리 요소 내 리스트 값
print(dictionary["ingredient"][0])
print()

# 딕셔너리 내 요소 추가
dictionary["price"] = 5000
print(dictionary)
print()

# 딕셔너리 내 요소 삭제
del dictionary["type"]
print(dictionary)