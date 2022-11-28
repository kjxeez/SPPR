from cvxopt.modeling import variable, op
import time

start = time.time()


def meow(a, b, c):
    print("Рассмотрим решение данной транспортной задачи:")
    print('[   ]',b)
    for i in range(0, 5):
        print("[",a[i],"]", c[5 * i:5 * i + 5])
    x = variable(25, 'x')  # список объёмов перевозимых товаров, обеспечивающих минимальные затраты

    z = (c[0] * x[0] + c[1] * x[1] + c[2] * x[2] + c[3] * x[3] + c[4] * x[4] + c[5] * x[5] + c[6] * x[6] + c[7] * x[7] +
         c[
             8] * x[8] + c[9] * x[9] + c[10] * x[10] + c[11] * x[11] + c[12] * x[12] + c[13] * x[13] + c[14] * x[14] +
         c[15] * x[
             15] + c[16] * x[16] + c[17] * x[17] + c[18] * x[18] + c[19] * x[19] + c[20] * x[20] + c[21] * x[21] + c[
             22] *
         x[22] + c[23] * x[23] + c[24] * x[24])
    mass1 = (x[0] + x[1] + x[2] + x[3] + x[4] <= a[0])  # х из строк таблицы (1 строка)

    mass2 = (x[5] + x[6] + x[7] + x[8] + x[9] <= a[1])  # х из строк таблицы (2 строка)

    mass3 = (x[10] + x[11] + x[12] + x[13] + x[14] <= a[2])  # х из строк таблицы (3 строка)

    mass4 = (x[15] + x[16] + x[17] + x[18] + x[19] <= a[3])  # х из строк таблицы (4 строка)

    mass5 = (x[20] + x[21] + x[22] + x[23] + x[24] <= a[4])  # х из строк таблицы (5 строка)

    mass6 = (x[0] + x[5] + x[10] + x[15] + x[20] == b[0])  # х из столбцов (1 столбец)

    mass7 = (x[0 + 1] + x[5 + 1] + x[10 + 1] + x[15 + 1] + x[20 + 1] == b[1])  # х из столбцов (2 столбец)

    mass8 = (x[0 + 2] + x[5 + 2] + x[10 + 2] + x[15 + 2] + x[20 + 2] == b[2])  # х из столбцов (3 столбец)

    mass9 = (x[0 + 3] + x[5 + 3] + x[10 + 3] + x[15 + 3] + x[20 + 3] == b[3])  # х из столбцов (4 столбец)

    mass10 = (x[0 + 4] + x[5 + 4] + x[10 + 4] + x[15 + 4] + x[20 + 4] == b[4])  # х из столбцов (5 столбец)
    x_non_negative = (x >= 0)
    problem = op(z, [mass1, mass2, mass3, mass4, mass5, mass6, mass7, mass8, mass9, mass10,
                     x_non_negative])  # условие неотрицательности
    print(problem)
    problem.solve(solver='glpk')

    try:
        for i in range(0, 5):
            print(*x.value[5 * i:5 * i + 5], sep='     ')
            print()

        print("\033[32mРешение найдено\033[39m")

        print("Стоимость доставки:\n", problem.objective.value()[0])
        stop = time.time()
        print("Время :")
        print(stop - start)
    except:
        print("\033[31mРешений у данной транспортной задачи нет\033[39m")


c1 = [1, 5, 7, 9, 3,
      4, 6, 4, 7, 13,
      1, 5, 3, 4, 9,
      2, 4, 2, 10, 3,
      3, 2, 5, 6, 4]  # список стоимости перевозки единицы товара от заказчиков к потребителям
a1 = [10, 20, 10, 30, 10]  # вертикаль
b1 = [10, 10, 25, 25, 30]  # горизонталь
meow(a1, b1, c1)

c2 = [4, 5, 2, 4, 3,
      3, 1, 3, 5, 2,
      2, 5, 3, 4, 6,
      3, 4, 2, 10, 9,
      1, 6, 9, 2, 7]  # список стоимости перевозки единицы товара от заказчиков к потребителям
a2 = [10, 10, 20, 20, 10]  # вертикаль
b2 = [5, 5, 10, 10, 5]  # горизонталь
meow(a2, b2, c2)
