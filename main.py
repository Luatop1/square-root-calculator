import math
while True:
    a = float(input("Введите а:"))
    if a == 0: # Проверка на решимость уравнения
        print("Ошибка! Коэффициент 'a' не может быть нулём")
        break
    b = float(input("Введите б:"))
    c = float(input("Введите с:"))

    d = b**2 - 4 * a * c # Дискриминант
    print(f"Дискриминант: {d}")

    if d < 0:
        print(f"Данная программа пока что не может решить уравнение с отрицательным дискриминантом, Дискриминант = {d}")
        break
    elif d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print(f"x¹ = {x2}, x² = {x1}")