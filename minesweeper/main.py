"""
Это не совсем "Сапёр", мы просто генерируем поле и заполняем поле минами, затем выводим полученное поле
Размеры поля и кол-во мин -> ввод три числа через пробел, например: 5 5 3
Куда поставить мину -> ввод 2 числа через пробел, координаты клетки, например: 2 5
Вывод результата -> "цифра": кол-во мин вокруг клетки, "*": мина, ".": пустая клетка
"""

n, m, k = (int(i) for i in input("Задайте размеры поля и кол-во мин: ").split())  # чтение размеров поля и числа мин
a = [[0 for j in range(m)] for i in range(n)]  # заполнение поля нулями
print(a)

for i in range(k):
    """
    тут вычитаем еденицу, чтобы row и col начинались с нуля, т.к. позиция в списках начинается с 0,
    если пользователь вводит 2 5, тогда это будет сооствествовать координат 1 4 на поле,
    а ввод 1 1 соответсвует 0 0 тоесть первой ячейке в первом столбце
    """
    row, col = (int(i) - 1 for i in input("Куда поставить мину: ").split())
    a[row][col] = -1  # расставляем мины
    print(a)

for i in range(n):
    for j in range(m):
        if a[i][j] == 0:  # в этой клетке мины нет, поэтому считаем число мин вокруг, тоесть сверху, снизу и т.д.
            for di in range(-1, 2):  # от -1 до 1
                for dj in range(-1, 2):
                    ai = i + di
                    aj = j + dj
                    # (ai, aj) проверим что клекта находится на поле(не выходит за границы) и в этой клекте находится -1
                    if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == -1:
                        a[i][j] += 1  # увеличиваем число, кол-во мин вокруг этой клетки

# вывод результата
print("Результат:  ")
for i in range(n):
    for j in range(m):  # перебор элементов в строке
        if a[i][j] == -1:
            print("*", end="")
        elif a[i][j] == 0:
            print(".", end="")
        else:
            print(a[i][j], end="")
    print()  # переход на новую строку
