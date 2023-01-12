# 2.1 Определить функцию, которая проверяет является ли строка, введенная пользователем, целым числом. Решение задачи сдать ссылкой на GitHub.
def proverca(string):
    try:
        int(string)
        return "Целое число"
    except ValueError:
        return "Другой тип данных"

print(proverca(input("Введите строку или численное значение: ")))

# 2.2 Даны две строки. Определить функцию, которая будет находить индекс второго вхождения второй строки в первую. Если подстрока ' ' вывести None. Решение сдать ссылкой на GitHub.
#Input:                                 Output:
# func('marry', 'r')            --> 3
# func('merry christmas', 's')  --> 14
# func('happy new year', ' ')   --> None
def func(a, b):
    if a.find(b, a.find(b) + 1):
        if b == ' ':
            return None
        elif a.count(b) > 1:
            i = a.find(b, a.find(b) + 1)
            return i
print(func('merry christmas', 's'))