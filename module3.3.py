def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(b=25)
print_params(c=[1, 2, 3])

value_list=[1, 'night', False]
values_dict = {'a': 1,'b': 'day', 'c': True }
print_params(*value_list)
print_params(**values_dict)

value_list2 = [[88, 12],89]
print_params(*value_list2,   42)