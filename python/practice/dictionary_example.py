#dictionary example
key_list = ["name", "hp", "mp", "level"]
value_list = ["기사", 200, 30, 5]

character = {}

for key in range(len(key_list)):
    character[key_list[key]] = ""

for value in range(len(value_list)):
    character[key_list[value]] = value_list[value]
    

print(character)