num = int(input("Введите число (от 1 до 100000): "))
if num <= 0 or num > 100000:
    print("Число должно быть от 1 до 100000")
else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, "является простым числом")
    else:
        print(num, "является составным числом")
