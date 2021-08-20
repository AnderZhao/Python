from random import randint

lists = []
count = 5
while count > 0:
    lists.append(randint(1, 20))
    count = count - 1

for list in lists:
    print list