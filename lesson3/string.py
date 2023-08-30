# string format
students_count = 15
genera_rate = 99.5
group_name = 'qa auto 22.08'

# format
# print('{} {} {}'.format(students_count, genera_rate, group_name))
# print('{2} {0} {1}'.format(students_count, genera_rate, group_name))
# print('{0:^10d} {1:.2f} {2:s}'.format(students_count, genera_rate, group_name))

# f-string
print(f'{students_count} {genera_rate:.3f} {group_name}')

# index
letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[0])

# slice (start: end: steз)
print(letters[3:-3:2])
print(letters[::-1])

# length
print(len(letters))

# split
python_str = '   python, is awesome.....'
python_str2 = 'python == is awesome'

my_list = python_str.split()
my_list2 = python_str2.split('==')
print(my_list)

# join
names_list = ["kate", "john"]
hello = 'hello'
print(' '.join(names_list))
print(' * '.join(hello))

# strip
python_str = '   python, is awesome.....'
print(python_str.strip(' .'))

# replace
python_str = 'python is awesome'
print(python_str.replace('python', 'JS'))
print(python_str.replace(' ', '...', 2))

# other methods
python_str = 'Python is awesome'
print(python_str.count('a'))
print(python_str.startswith('p'))
print(python_str.index('a'))
print(python_str.upper())
print(python_str.title())
print(python_str.swapcase())

number_str = '100'
print(number_str.isdigit())
print(number_str.isnumeric())
print(number_str.isascii())
