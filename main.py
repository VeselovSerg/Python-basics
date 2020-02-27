from sys import argv
from functools import reduce
from itertools import count, cycle

# 1.


script_name, work_time, salary_in_hour, bonus = argv


def salary():
    try:
        result = float(work_time) * float(salary_in_hour) + float(bonus)
        print(f'Worker salary is {result}.')
    except ValueError:
        return print('Need a number')


salary()

# 2.


orig_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
my_lst = [n for i, n in enumerate(orig_list) if orig_list[i] > orig_list[i - 1] and i != 0]
print(my_lst)

# 3.


my_list = [n for n in range(20, 241) if n % 20 == 0 or n % 21 == 0]
print(my_list)

# 4.

my_list1 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
sort_list = [n for n in my_list1 if my_list1.count(n) == 1]
print(sort_list)

# 5.


my_list2 = [n for n in range(100, 1001) if n % 2 == 0]
print(reduce(lambda a, b: a + b, my_list2))

# 6.


for n in count(int(input('Enter x for the loop from x to 100: '))):
    if n > 100:
        break
    else:
        print(n)

lst = [1, 5, 'a', 'y', False, 'FG', 3467]
i = int(input('Enter x for the loop of list from x to 100: '))
for n in cycle(lst):
    if i > 100:
        break
    else:
        print(n)
        i += 1


# 7.


def fact(n):
    a = 1
    for i in range(1, n + 1):
        a *= i
        yield a


for n in fact(int(input('Enter a factorial number: '))):
    print(n)
