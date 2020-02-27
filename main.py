# 1.

def division(a, b):
    while True:
        try:
            a = float(a)
            b = float(b)
            return print(f'The division of {a} and {b} is {a / b}')
        except ZeroDivisionError:
            b = input('You can`t divide by 0, enter new divider: ')
        except ValueError:
            a = input('Error! You need enter a number. Try again. a = ')
            b = input('b = ')


def division_use():
    division(input('Input a number you want to divide: '), input('Input a divider: '))


division_use()


# 2.


def profile(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} = {value}')


def profile_use():
    profile(name=input('Enter your name: '),
            surname=input('Enter your surname: '),
            birthday=input('Date of birth: '),
            city=input('Your city: '),
            email=input('Enter email: '),
            phone=input('Phone number: '))


profile_use()


# 3.


def my_func(arg1, arg2, arg3):
    args = (arg1, arg2, arg3)
    return sum(args) - min(args)


def my_func_use():
    my_func(int(input('Enter first integer number: ')),
            int(input('Enter second integer number: ' )),
            int(input('Enter third integer number: ')))


my_func_use()


# 4.


def pow_func(x, y):
    return x ** abs(y)


print(pow_func(3, -4))


def new_pow_func(x, y):
    y = abs(y)
    if y == 0:
        return 1
    else:
        return x * new_pow_func(x,y-1)


print(new_pow_func(3, -4))


# 5.


def sum_numbers():
    result = 0
    while True:
        numbers = input('Enter list of number or x to exit: ').split()
        for i in numbers:
            try:
                if i == 'x':
                    print(f'Sum is {result}.')
                    return
                else:
                    result += int(i)
            except ValueError:
                print('Enter number or x')
        print(f'Sum is {result}')


sum_numbers()


# 6.


def int_func(text):
    new_text = text[0].title()+ text[1:len(text)]
    return new_text


def int_func_use():
    print(int_func(input('Enter text: ')))


int_func_use()


def new_int_func(new_text):
    text = []
    sep = ' '
    for i in range (len(new_text)):
        text.append(int_func(new_text[i]))
    return sep.join(text)


def new_int_func_use():
    print(new_int_func((input('Enter phrase: ').split(" "))))


new_int_func_use()
