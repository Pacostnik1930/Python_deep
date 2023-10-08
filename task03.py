from random import randint


LOWER_LIMIT = 0
UPPER_LIMIT = 1000
num = randint(LOWER_LIMIT, UPPER_LIMIT)
for i in range(10):
    guess = int(input("Угадайте число от {} до {}: ".format(LOWER_LIMIT, UPPER_LIMIT)))
    if guess == num:
        print("Вы угадали число!")
        break
    elif guess < num:
        print("Загаданное число больше")
    else:
        print("Загаданное число меньше")
else:
    print("Вы не угадали число. Было загадано", num)