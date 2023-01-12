# 1.1 Реализовать Рекурсию. Возведение числа x в степень y
def exponentiation(x, y):
    if y == 1:
        return x
    if y == 0:
        return 1
    else:
        return x ** y
x = float(input("Введите число возводимое в степень: "))
y = float(input("Введите степень: "))
print(exponentiation(x, y))

# 1.2 Определить функцию, которая будет дублировать нули в списке и вернуть в виде итеррируемого объекта-коллекции.
#Input:                         Output:
# func([0,0,0])            --> [0,0,0,0,0,0]
# func([1,2,100,0,3,4,5,0])--> [1,2,100,0,0,3,4,5,0,0]
def duplicate(func):
    a = []
    for i in func:
        a.append(i)
        if i == 0:
            a.append(0)
    return a
print(duplicate([0,0,0]))
