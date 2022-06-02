# print("Задача 1")
# print("Найти НОК двух чисел")

# number_1 = int(input("Введите первое число: "))
# number_2 = int(input("Введите второе число: "))

# def s_c_m(x, y):
#     if x > y:
#         bigger = x
#     else:
#         bigger = y

#     while (True):
#         if ((bigger % x == 0) and (bigger % y == 0)):
#             scm = bigger
#             break
#         bigger += 1
#     return scm

# print(f'НОК {number_1} и {number_2} = {s_c_m(number_1, number_2)}')

# print()
# print("Задача 2")
# print("Вычислить число Пи c заданной точностью d")
# # Пример: при d = 0.001,  c= 3.141.

# count_of_symbols = input("Введите необходимое число знаков после запятой: ")
# # Если для указания точности используется десятичная дробь, то высчитываем число зннаков после запятой.
# if count_of_symbols.find(".") > (-1):
#     count_of_symbols = abs(count_of_symbols.find('.') -
#                            len(count_of_symbols)) - 1
# count_of_symbols = int(count_of_symbols)
# k = 1
# s = 0

# for i in range(1000000):
#     if i % 2 == 0:
#         s += 4 / k
#     else:
#         s -= 4 / k
#     k += 2

# s = str(s)
# # Первые 2 символа строки - это "3.". Поэтому, чтобы отобразить необходимое количество знаков после запятой, нужно отобразить на 2 символа больше.
# s = float(s[:(count_of_symbols + 2)])
# print(s)

# print()
# print("Задача 3")
# print("Составить список простых множителей натурального числа N.")

# number = int(input("Введите натуральное число: "))
# mults = []
# d = 2

# while d * d <= number:
#     if number % d == 0:
#         mults.append(d)
#         number //= d
#     else:
#         d += 1
# if number > 1:
#     mults.append(number)
# print(mults)

# print()
# print("Задача 4")
# print(
#     "Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности."
# )
# # Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]
# orignal_line = [1, 2, 3, 5, 1, 5, 3, 10]
# print(f'Исходный список: {orignal_line}')
# new_line = []

# for i in orignal_line:
#     if i not in new_line:
#         new_line.append(i)
# print(f'Список без повторяющихся элементов: {new_line}')

# print()
print("Задача 5")
print(
    "Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа."
)
import random

# заполним файл случайными числами
with open('file.txt', 'a') as insert_data:
    for i in range(100):
        i = random.randint(-100, 100)
        insert_data.write(str(i))
        insert_data.write('\n')
    insert_data.write('\n')

with open('file.txt', 'r') as read_data:
    numbers = read_data.readlines()

print(numbers)
with open('file.txt', 'a') as return_data:
    return_data.writelines("Обновлённый список \n")
    for i in numbers:
        if int(i) % 2 != 0:
            return_data.writelines(i)