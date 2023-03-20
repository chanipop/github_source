# file_write
import random

hanguls = list("가나다라마바사아자차카타파하")
# print(hanguls)

with open("info.txt", "w", encoding="UTF-8") as file:
    for i in range(1000):
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40, 100)
        height = random.randrange(140, 200)
        file.write(f"{name}, {weight}, {height}\n")