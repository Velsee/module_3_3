def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

# Вывод значений параметров
print_params()

# Вызываем функцию print_params с разным количеством аргументов, включая вызов без аргументов.
print_params(2, 'столбец', False)
print_params(3, 'None')
print_params(a='один', b='два', c='три')
print_params(a='один', b='два')
print_params(b='два', c='три')
print_params(a='один', c='три')
print_params(a='один')
print_params(b='два')
print_params(c='три')
print_params(c = [1, 2, 3])

# Вывод функции без аргументов
print_params()

# Проверяем, работают ли вызовы print_params(b = 25) и print_params(c = [1,2,3])
print_params(b=25)
print_params(c=[1, 2, 3])

# Распаковка параметров
values_list = [1, "hello", 3.14]
values_dict = {'a': 2, 'b': False , 'c': 'ночь'}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)