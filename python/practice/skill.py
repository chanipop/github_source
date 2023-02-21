character = {
    "name" : "기사",
    "level" : 12,
    "items" : {
        "sword" : "불꽃의 검",
        "armor" : "풀플레이트"
    },
    "skill" : ["베기", "세게 베기", "아주 세게 베기"]
}

for key in character :
    if type(character[key]) is str:
        print(key, " : ", character[key])
    if type(character[key]) is int:
        print(key, " : ", character[key])
    if type(character[key]) is dict:
        for key2 in character[key]:
            print(key2, " : ", character[key][key2])
    if type(character[key]) is list:
        for key3 in character[key]:
            print(key, " : ", key3)
