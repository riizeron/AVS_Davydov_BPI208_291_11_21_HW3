from extender import *


def ReadStrArray(container, strArray):
    arrayLen = len(strArray)
    i = 0  # Индекс, задающий текущую строку в массиве
    figNum = 0
    while i < arrayLen:
        str = strArray[i]
        key = int(str)  # преобразование в целое
        # print("key = ", key)
        if key == 1:  # признак прямоугольника
            i += 1
            number = Complex()
            i = number.ReadStrArray(strArray, i)  # чтение комплексного числа с возвратом позиции за ним
        elif key == 2:  # признак треугольника
            i += 1
            number = Fraction()
            i = number.ReadStrArray(strArray, i)  # чтение дроби с возвратом позиции за ней
        elif key == 3:
            i += 1
            number = Polar()
            i = number.ReadStrArray(strArray, i)  # чтение полярной координаты с возвратом позиции за ней
        else:
            # что-то пошло не так. Должен быть известный признак
            # Возврат количества прочитанных фигур
            return figNum
        # Количество пробелами чисел увеличивается на 1
        if i == 0:
            return figNum
        figNum += 1
        container.store.append(number)
    return figNum
