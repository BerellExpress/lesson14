# 1)
#def print_params(a=1, b='строка', c=True):
    #print(a, b, c)

# print_params(1, 2, 3, 4 ) - ошибка TypeError: print_params() takes from 0 to 3 positional arguments but 4 were given
# print_params(b = 25) - работает, вывод на консоль: 1 25 True
# print_params(c = [1,2,3]) - работает, вывод на консоль: 1 строка [1, 2, 3]

# 2)
def print_params(a=1, b='строка', c=True):
    print(a, b, c)

values_list = [123, False, 'строка2']
values_dict = {'a': 3, 'b': 2, 'c': 1}

print_params(*values_list)
print_params(**values_dict)
# 3)
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)