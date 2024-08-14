def collatz(num):
    if num % 2 == 0:
        print(num // 2)
        return num // 2

    elif num % 2 == 1:
        print(num * 3 + 1)
        return num * 3 + 1

r = int(input())
while r !=1:
    r = collatz(r)
   



