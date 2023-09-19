import os

root_folder = '/Users/yevheniab/PycharmProjects/homework'

largest_file_name = ''
largest_file_size = 0

file_info_list = []

for dirpath, dirnames, filenames in os.walk(root_folder):
    for filename in filenames:
        file_path = os.path.join(dirpath, filename)
        file_size = os.path.getsize(file_path)

        file_info_list.append((filename, file_size))

        if file_size > largest_file_size:
            largest_file_size = file_size
            largest_file_name = filename

with open('files_size.txt', 'w') as file_size_file:
    for filename, file_size in file_info_list:
        file_size_file.write(f"{filename}: {file_size} bytes\n")

print(f"Largest File: {largest_file_name}")
print(f"Size: {largest_file_size} bytes")
