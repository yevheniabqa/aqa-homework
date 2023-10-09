import time


# Decorator for measuring execution time
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.6f} seconds")
        return result

    return wrapper


@timing_decorator
def make_big_number(number):
    return number ** 100

if __name__ == "__main__":
    print(make_big_number(17))
