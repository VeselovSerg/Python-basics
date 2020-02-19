# 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

user_name = input('Please, input your name: ')
first_number = float(input(f'{user_name}, input any number: '))
second_number = float(input(f'{user_name}, input another number: '))
sign = input(f'{user_name}, input one of this signs " /, *, -, +": ')
if sign == '/':
    if second_number != 0:
        print(f'{user_name}, division of {first_number} and {second_number} is {first_number / second_number}')
    else:
        print("You can't divide by 0!")
if sign == '*':
    print(f'{user_name}, multiplication of {first_number} and {second_number} is {first_number * second_number}')
if sign == '-':
    print(f'{user_name}, subtraction of {first_number} and {second_number} is {first_number - second_number}')
if sign == '+':
    print(f'{user_name}, addition of {first_number} and {second_number} is {first_number + second_number}')

# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

seconds = int(input(f'{user_name}, now please input value in seconds: '))
minutes = seconds // 60
hours = minutes // 60

print(f'You input value of {seconds} seconds this is the same as {hours:02d}:{minutes % 60:02d}:{seconds % 60:02d}')

# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = input('Now please input one number: ')
print(f'You input a number {n}. The {n} + {n + n} + {n + n + n} is {int(n) + int(n + n) + int(n + n + n)}')

# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

max_number = int(input('Now, please, input big number: '))
find_number = max_number % 10
max_number = max_number // 10
while max_number > 0:
    if max_number % 10 > find_number:
        find_number = max_number % 10
    max_number = max_number // 10
print(f'The largest number is {find_number}.')

# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите
# прибыль фирмы в расчете на одного сотрудника.

revenue = int(input(f'{user_name}, введите вашу выручку! Не бойтесь, мы не позвоним в налоговую... '))
costs = int(input(f'{user_name}, введите ваши издержки, не стесняйтесь: '))
if revenue > costs:
    print(f'{user_name}, вы отличный предприниматель, ваша фирма заработала {revenue - costs}!')
elif revenue < costs:
    print(f'{user_name}, у вас убыток в {abs(revenue - costs)}, видимо не удачный год?..')
else:
    print(f'{user_name}, вы на нуле..')

number_of_workers = int(input(f'{user_name}, сколько людей у вас в фирме? '))
print(f'{user_name}, в среднем каждый сотрудник приносит вам {(revenue - costs) / number_of_workers}.')

# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
#
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

a = int(input(f'{user_name} сколько вы сейчас пробегаете километров в день?'))
b = int(input(f'{user_name} сколько вы хотите пробегать в день?'))
days = 0
while a < b:
    a = a * 1.1
    days = days + 1
print(f'{user_name}, если вы будете увеличивать ваш результат на 10% в день,'
      f' то через {days} дней, вы достигнете результата!')
