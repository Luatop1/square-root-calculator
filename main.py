import math
while True:
    try:
        abc = input("Введите коофиценты a, b, c через запятую, например:(1, 2, 3):")
        abc = abc.split(",")
        a = float(abc[0])
        b = float(abc[1])
        c = float(abc[2])
    except:
        print("Введите числа правильно!")
        continue

    if b < 0: # Проверка на отрицательность
        b_symbol = "-"
        b_modul = abs(b)
    else:
        b_symbol = "+"
        b_modul = abs(b)

    if c < 0: # Проверка на отрицательность
        c_symbol = "-"
        c_modul = abs(c)
    else:
        c_symbol = "+"
        c_modul = abs(c)

    equation = f"{float(a)}x² {b_symbol} {float(b_modul)}x {c_symbol} {float(c_modul)} = 0"
    print(equation)

    d = b**2 - 4 * a * c # Дискриминант
    print(f"Дискриминант: {d}")

    if d < 0:
        print(f"Данная программа пока что не может решить уравнение с отрицательным дискриминантом, Дискриминант = {d}")
    elif d == 0:
        x = (-b) / (2 * a)
        print(d)
    else:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print(f"x¹ = {x2}, x² = {x1}")

    while True:
        ask_solution = input("Нужно пошагавое решение? [y/n]")
        if ask_solution == "y" and d > 0:
            print(f"1. Вот само уравнениу {equation}")
            print(f"2. Находим дискриминант D = {b}² - 4 * {a}* {c} = {d}")
            print(f"3. Находим первый корень x¹ = (-{b_modul} + √{d}) / (2* {a} ) = {x2}")
            print(f"4. Находим второй корень x² = (-{b_modul} - √{d}) / (2* {a} ) = {x1}")
            print("Решишь новое уравнение?")
            break
        elif ask_solution == "n":
            break
        elif d < 0:
            print("Решение не может быть предоставленым с дискриминантом меньше нуля")
            break