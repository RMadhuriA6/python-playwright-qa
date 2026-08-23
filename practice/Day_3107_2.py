try:
    print(int('hello'))
except ValueError:
    print('Give correct literal value')


try:
    print(int('hello'))
except TypeError:
    print('Give correct literal value')


