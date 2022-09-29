print('=' * 100)

'''Задание 1'''
print("*" * 40, "Задание 1", "*" * 40)
'''Входные данные
Пользователь вводит строку.'''
txt = input("Введите предложение / строку: ")
print("-" * 100)
'''Выходные данные
Воспользуйтесь одним print(), но при этом выводите с новой строки:
 Сначала выведите третий символ этой строки.
 Во второй строке выведите предпоследний символ этой строки.
 В третьей строке выведите первые пять символов этой строки.
 В четвертой строке выведите всю строку, кроме последних двух символов.
 В пятой строке выведите все символы с четными индексами (считая, что индексация
начинается с 0, поэтому символы выводятся, начиная с первого символа).
 В шестой строке выведите все символы с нечетными индексами, то есть начиная со
второго символа строки.
 В седьмой строке выведите все символы в обратном порядке.
 В восьмой строке выведите все символы строки через один в обратном порядке, начиная с
последнего.
 В девятой строке выведите все символы строки через один в обратном порядке, начиная с
предпоследнего.
 В десятой строке выведите все символы в обратном порядке без первого и последнего
элемента.
 Ну, и напоследок выведите длину данной строки.'''

print(txt[2], txt[-2], txt[:5], txt[:-2], txt[0::2], txt[1::2], txt[::-1],
      txt[::-2], txt[-2::-2], txt[-2:0:-1], len(txt), sep='\n')
print("-" * 100)

'''Задание 2'''
print("*" * 40, "Задание 2", "*" * 40)

'''Пользователь вводит строку. Разрежьте её на две части – равные, если длина строки чётная, а
если длина строки нечётная, то длина первой части должна быть на один символ больше.
Переставьте эти две части местами, результат запишите в новую строку и выведите на экран.'''

'''Вариант А'''
fgf = input("Введите строку: ")
f1 = fgf[:len(fgf) // 2 + len(fgf) % 2]
f2 = fgf[len(fgf) // 2 + len(fgf) % 2:]
g = f2 + f1
print(g)

'''Вариант В'''
print(fgf[(len(fgf) + 1) // 2:] + fgf[:(len(fgf) + 1) // 2])
print("-" * 100)

'''Задание 3'''
print("*" * 40, "Задание 3", "*" * 40)

'''Пользователь вводит целое число. Требуется определить, является ли год с данным номером
високосным. Если год является високосным, то выведите YES, иначе выведите NO. Напомним, что
в соответствии с григорианским календарём, год является високосным, если его номер кратен 4,
но не кратен 100, а также если он кратен 400.'''

year = int(input("Enter any year: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("YES")
else:
    print("NO")

print("-" * 100)

'''Задание 4'''
print("*" * 40, "Задание 4", "*" * 40)

'''Даны три числа a, button, c. Определите, существует ли треугольник с такими сторонами. Если
треугольник существует, выведите строку YES, иначе выведите строку NO.'''

a = input("Сторона а: ")
b = input("Сторона button: ")
c = input("Сторона c: ")

if (a + b > c) or (a + c > b) or (b + c > a):
    print("YES")
else:
    print("NO")

print("-" * 100)

'''Задание 5'''
print("*" * 40, "Задание 5", "*" * 40)

'''Дано три числа. Упорядочите их в порядке возрастания. Программа должна считывать три
числа a, button, c, затем программа должна менять их значения так, чтобы стали выполнены
условия a <= button <= c, затем программа выводит тройку a, button, c.

Дополнительные ограничения: нельзя использовать дополнительные переменные.'''

# a = int(input())
# button = int(input())
# c = int(input())
# if a >= button:
#     a, button = button, a
# elif a >= c:
#     a, c = c, a
# elif button >= c:
#     button, c = c, button

print("?????????????????????????????????????????????????????????")

print("-" * 100)

'''Задание 6'''
print("*" * 40, "Задание 6", "*" * 40)

'''Даны три целых числа. Определите, сколько среди них совпадающих. Программа должна вывести
одно из чисел: 3 (если все совпадают), 2 (если два совпадает) или 0 (если все числа совпадают)'''

a = int(input())
b = int(input())
c = int(input())

if a == b == c:
   print(3)
elif a == b or b == c or a == c:
   print(2)
else:
   print(0)

print("-" * 100)


'''Задание 7'''
print("*" * 40, "Задание 6", "*" * 40)

'''
1) Напишите счетчик с помощью конструкции while, который выводит числа от 0 до 10.
2) Напишите счетчик с помощью конструкции while, который выводит числа от 20 до 1.
   Попробуйте вывести числа в одной строчке, разделённые пробелом
3) Напишите цикл while, в котором вы, если число чётное, каждую итерацию уменьшаете его
   в 2 раза. Вы делите целое чётное число на 2 пока от него не останется нечётный остаток.
   Посчитайте сколько раз вы делили нацело на 2.'''

'''task 1'''
a = 0
while a <= 10:
    print(a)
    a += 1



print("-" * 100)