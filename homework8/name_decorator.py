def log_function_name(func):
    def wrapper(*args, **kwargs):
        # get the name of decorated function
        func_name = func.__name__

        # call result
        result = func(*args, **kwargs)

        # print the function name and result
        print(f"Function '{func_name}' called. Result: {result}")

        # return the result
        return result

    return wrapper


# Apply the decorator to your arithmetic functions
@log_function_name
def add(a, b):
    return a + b


@log_function_name
def multiply(a, b):
    return a * b


# Call the decorated functions
result_add = add(5, 3)
result_multiply = multiply(4, 6)
