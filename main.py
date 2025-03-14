while True:
    try:
        import math

        while True:
            abc = input("Введите коофиценты a, b, c через запятую, например:(1, 2, 3):")
            abc = abc.split(",")
            a = float(abc[0])
            b = float(abc[1])
            c = float(abc[2])

            if b < 0:  # Проверка на отрицательность
                b_symbol = "-"
                b_modul = abs(b)
            else:
                b_symbol = "+"
                b_modul = abs(b)

            if c < 0:  # Проверка на отрицательность
                c_symbol = "-"
                c_modul = abs(c)
            else:
                c_symbol = "+"
                c_modul = abs(c)

            print(f"{float(a)}x² {b_symbol} {float(b_modul)}x {c_symbol} {float(c_modul)} = 0")

            d = b ** 2 - 4 * a * c  # Дискриминант
            print(f"Дискриминант: {d}")

            if d < 0:
                print(f"Данная программа пока что не может решить уравнение с отрицательным дискриминантом, Дискриминант = {d}")
                print("Попробуйте решить новое уравнение!")
            elif d == 0:
                x = (-b) / (2 * a)
                print(x)
            else:
                x1 = (-b + math.sqrt(d)) / (2 * a)
                x2 = (-b - math.sqrt(d)) / (2 * a)
                print(f"x¹ = {x2}, x² = {x1}")
    except:
        print("Произошла ошибка!")