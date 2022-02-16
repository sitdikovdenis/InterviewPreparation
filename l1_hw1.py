# Написать функцию, реализующую вывод таблицы умножения размерностью AｘB.
# Первый и второй множитель должны задаваться в виде аргументов функции.
# Значения каждой строки таблицы должны быть представлены списком, который формируется в цикле.
# После этого осуществляется вызов внешней lambda-функции, которая формирует на основе списка строку.
# Полученная строка выводится в главной функции. Элементы строки (элементы таблицы умножения) должны
# разделяться табуляцией.


print_table_line = lambda a, b, c: print(f'{a} * {b} = {c}')


def multiplication_table(a, b):
    multiplication_table_elems = []
    for i in range(a):
        for j in range(b):
            multiplication_table_elems.append([i + 1, j + 1, (i + 1) * (j + 1)])

    for elem in multiplication_table_elems:
        print_table_line(elem[0], elem[1], elem[2])


multiplication_table(6, 5)
