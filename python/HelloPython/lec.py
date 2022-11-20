# тип данных и переменная
# int, float, boolean, str, list, None

# value = None

# print(type(a))   # добавляем type, чтобы посмотреть тип переменной в терминале
# print(type(b))
# value = 12345
# print(type(value))
# s = 'hello \nworld'   # \n переход на новую строку 

# a = 123
# b = 1.23
# s = 'hello world'

# print(s)  # вывод строки
# print(a, '-' , b,'-', s)
# print('{} - {} - {}'.format(a, b, s))
# print(f'{a} - {b} - {s}')
# print('{1} - {2} - {0}'.format(a, b, s))

# f = False  # f = True
# print(f)

# list = [1, 2, 3]
# list = ['hello', 'world', '!!!']  # вывод строк
# print(list)

# print('Введите a');
# a = input()             #10
# print('Введите b');
# b = input()             #20
# print(a, ' + ', b, '=' , a+b) # 10 + 20 = 1020 - это данные в строчном формате
# print('{} {}'.format(a, b))
# print(f'{a} {b}')

# print('Введите a');
# a = int(input())         # чтобы получить данные в числовом формате (целое число) добавляем int()
# print('Введите b');
# b = int(input())             
# print(a, ' + ', b, '=' , a+b)  # 10 + 20 = 30

# print('Введите a');
# a = float(input())         # чтобы получить вещественное значение добавляем float()
# print('Введите b');
# b = float(input())             
# print(a, ' + ', b, '=' , a+b)   # 1.5 + 2.8 = 4.3

# Арифметические операции
# +, -, *, /, %, //, **              // - это деление в целых числах  ** - возведение в степень
# **, ⊕, ⊖, *, /, //, %, +, -     % - остаток от деления
# (), Сокращенные операции 

# a = 1.312586123
# b = 3
# c = round(a * b, 7)   # round()  - округление по математическим правилам "," сколько знаков после запятой
# print(c) 

# a = 3
# a *= 5
# print(a) 

# Логические операции 
# >, >=, <, <=, ==, != 
# not, and, or – не путать с &, |, ^ 
# Кое-что ещё: is, is not, in, not in

# f = [1, 2, 3, 4]

# print(f)
# print(not 2 in f)

# is_odd = not f[0] % 2 
# print(is_odd)
 
# Использование оператора if, if-else
# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#    print(a)
# else:
#    print(b)

# Использование оператора if, elif, else
# username = input('Введите имя: ')
# if username == 'Alex' :
#    print('Ура, это же ALEX!')
# elif username == 'Alexia' :
#    print('Я так ждал Вас, Alexia!')
# elif username == 'Андрей' :
#    print('Андрей - ТОП)')
# else:
#    print('Привет,' , username)

# Используем оператор while

# original = 23
# inverted = 0
# while original != 0 :
#    inverted = inverted * 10 + (original % 10)
#    original //= 10
# print(inverted)


# Используем оператор while-else

# original = 23
# inverted = 0
# while original != 0 :
#    inverted = inverted * 10 + (original % 10)
#    original //= 10
# else:
#    print('Пожалуй')
#    print('хватит)')
# print(inverted)

# Используем цикл for

# for i in 1,2,3,4,5:
#    print(i**2)

# list = [1,2,3,4,10,5]
# for i in list:
#    print(i)

# r = range(10)
# for i in r:
#    print(i)

# for i in range(1, 5):    # вывод чисел от 1 до 4
#    print(i)

# for i in range(1,10, 2):   # вывести цифры в диапазоне от 1 до 10 с шагом 2 т.е. 1, 3, 5, 7, 9
#    print(i)

# for i in 'qwe - rty':
#    print(i)

# Работа со строками

# text = 'съешь ещё этих мягких французских булок'
# print(len(text))                   # 39
# print('ещё' in text)               # True
# print(text.isdigit())              # False
# print(text.islower())              # True
# print(text.replace('ещё', 'ЕЩЕ'))

# for c in text:
#    print(c)

# help(str)         # Получить справку про функцию str

'''text = 'съешь ещё этих мягких французских булок'
print(text[0])                     # с
print(text[1])                     # ъ
print(text[len(text)- 1])          # к
print(text[-5])                    # б
print(text[:])                     # съешь ещё этих мягких французских булок
print(text[:2])                    # съ
print(text[len(text)- 2:])         # ок
print(text[2:9])                   # ешь ещё
print(text[6:-18])                 # ещё этих мягких
print(text[0:len(text):6])         # сеикакл
print(text[::6])                   # сеикакл
text = text[2:9] + text[-5] + text[:2]  '''

# Списки 

'''numbers = [1, 2, 3, 4, 5]
print(numbers)         # [1, 2, 3, 4, 5]
ran = range(1, 6)
print(type(ran))       # <class 'range'>
numbers = list(ran)    # приведение типа range к типу list
print(type(numbers))   # <class 'list'>

print(numbers)         # [1, 2, 3, 4, 5]
numbers[0] = 10
print(f'{len(numbers)} len')   # 5 len
print(numbers)                 # [10, 2, 3, 4, 5]
for i in numbers:
    i *= 2
    print(i)                  # [20, 2, 3, 4, 5]
print(numbers)                # [10, 2, 3, 4, 5] '''

'''colors = ['red', 'green', 'blue']

for e in colors:
    print(e)     # red green blue

for e in colors:
    print(e*2)     # redred greengreen blueblue

colors.append('gray')  # добавить в конец
print(colors)          # ['red', 'green', 'blue', 'gray']
print(colors == ['red', 'green', 'blue', 'gray'])  # True
colors.remove('red') # del colors[0] - удалить элемент
print(colors)     # ['green', 'blue', 'gray'] '''

# Функции

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

arg = 3
print(f(arg))
print(type(f(arg)))
