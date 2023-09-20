import sum_range
import square
import rectangle
import map_func

# sum range (task 1)
start = int(input('Range: Enter a start number: '))
end = int(input('Range: Enter an end number: '))

if __name__ == '__main__':
    result = sum_range.sum_of_range(start, end)
    print(f"The sum of integers from {start} to {end} is {result}")

# rectangle (task 3)
width = 5
height = 4
character = 'x'
if __name__ == '__main__':
    rectangle.display_box(width, height, character)

# square (task 2)
side_length = float(input("Enter the side length of the square: "))

if __name__ == '__main__':
    perimeter, area, diagonal = square.squares(side_length)

print(f"Perimeter of the square: {perimeter}")
print(f"Area of the square: {area}")
print(f"Diagonal of the square: {diagonal}")

# my map (task 4)
def squared(x):
    return x * x

numbers = [1, 2, 3, 4, 5]

if __name__ == '__main__':
    squared_numbers = map_func.my_map(squared, numbers)

print('Map function is called here: ', squared_numbers)  # Output: 1, 4, 9, 16, 25


