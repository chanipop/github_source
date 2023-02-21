# 딕셔너리 키 값 인풋 받아서 확인하기
dictionary = {
    "key1" : "123",
    "key2" : "456",
    "key3" : "789",
    "key4" : "10"
}

key = input("> Key값을 입력하세요. : ")

if key in dictionary:
    print(dictionary[key])
else:
    print("잘못된 Key값에 접근하고 있습니다.")