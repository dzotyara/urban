# Практическая работа по уроку "Динамическая типизация"
# Цель: Написать программу на языке Python, используя Pycharm, для демонстрации динамической типизации.

# 2. Создайте переменные разных типов данных:
#   - Создайте переменную name и присвойте ей значение вашего имени (строка).
#   - Выведите значение переменной name на экран.
#   - Создайте переменную age и присвойте ей значение вашего возраста (целое число).
#   - Выведите значение переменной age на экран.
#   - Перезапишите в age текущее значение переменной age + новое.
# Как неверно (просто перезапись на новое число):
# a = 15
# a = 17
#   - Выведите измененное значение переменной age на экран.
#   - Создайте переменную is_student и присвойте ей значение True (логическое значение).
#   - Выведите значение переменной is_student на экран.

name = input("Введите ваше имя: ")
age = int(input("Введите ваш возраст: "))
ageSecond = age + 1
is_student = True


print(f'Ваше имя: {name}\nВаш возраст: {age} лет\nВаш новый возраст: {ageSecond} лет\nIs Student: {is_student}')