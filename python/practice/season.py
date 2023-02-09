import datetime

now = datetime.datetime.now()
month = now.month

if month / 3 <= 1 :
    # print("1/4 QUARTER")
    raise NotImplementedError
elif month / 3 <= 2 :
    print("2/4 QUARTER")

elif month / 3 <= 3 :
    print("3/4 QUARTER")

else :
    print("4/4 QUARTER")