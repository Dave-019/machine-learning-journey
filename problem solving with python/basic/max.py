def print_max(a, b):
    if a > b:
        return a
    else:
        return b

x = eval(input('Enter a number: '))
y = eval(input('Enter another number: '))

print(print_max(x, y))
