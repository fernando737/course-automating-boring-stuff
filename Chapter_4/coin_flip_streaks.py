import random
numberOfStreaks = 0
lst = []
for experimentNumber in range(100):
    lst.append("T") if random.randint(0,1) else lst.append("H")

streak_count = 0
for y in range(99):
    if lst[y] == lst[y+1]:
        streak_count +=1
        if streak_count == 5:
            numberOfStreaks +=1
    else:
        streak_count = 0

print(lst)
print(len(lst))
print(numberOfStreaks)
print('Chance of streak: %s%%' % (numberOfStreaks/100))