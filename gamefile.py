import random


def gameres(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == "w":
        if you == "s":
            return False
        elif you == "g":
            return True
    elif comp == 'g':
        if you == 's':
            return False
        elif you == "w":
            return True


print("let's play snake water and gun game!!!")
p1 = input("kindly enter your name: ")
a = True
b = 0
c = 0
d = 0
comp = ''
for i in range(1, 11):
    rando = random.randint(1, 3)
    print("computer turn: choose snake(s),water(w),gun(g) :")
    if rando == 1:
        comp = 's'
    elif rando == 2:
        comp = 'w'
    elif rando == 3:
        comp = 'g'
    you = input("your turn: choose snake(s),water(w),gun(g) :")
    print(f"computer has chosen {comp}")
    print(f"{p1} has chosen {you}")
    a = gameres(comp, you)

    if a is None:
        # print("match tie..!")
        d += 1
    elif a:
        b += 1
    # print("you win")
    else:
        c += 1
    # print("you lose")
if b > c:
    print("you win")
elif d == 10:
    print("match tie...!")
else:
    print("you lose..!")
print(p1+" your score: " + str(b))
print("computer score: " + str(c))
print(f"{d} times your choices are matched..!!")
