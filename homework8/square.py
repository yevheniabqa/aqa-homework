from time_decorator import timing_decorator


# Generator function to yield squares of even numbers
@timing_decorator  # timing decorator used here to evaluate performance and monitor it
def generate_even_squares():
    for num in range(0, 1000000001, 2):
        yield num ** 2


if __name__ == "__main__":
    for square in generate_even_squares():
        print(square)
