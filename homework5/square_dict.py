str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

int_list = list(map(lambda x: int(x), str_list))

squared_dict = dict(zip(int_list, map(lambda x: x ** 2, int_list)))

print(squared_dict)
