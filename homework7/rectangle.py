def display_box(width: int, height: int, character="*"):
    print(character * width)

    for _ in range(height - 2):
        print(character + " " * (width - 2) + character)

    if height > 1:
        print(character * width)


