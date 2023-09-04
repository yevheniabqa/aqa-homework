
text_input = input("Enter text separated by spaces: ")

word_list = text_input.split()

if len(word_list) >= 3:
    last_three_elements = word_list[-3:]
    print("Last 3 elements:", last_three_elements)
else:
    print(f"The number of elements is less than 3. There are {len(word_list)} elements in the current list.")
