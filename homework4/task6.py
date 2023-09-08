input_string = input("Enter a string: ")

char_count = {}

for char in input_string:
    char_count[char] = char_count.get(char, 0) + 1

char_count_strings = [f"{char},{count}" for char, count in char_count.items()]

print(' '.join(char_count_strings))



