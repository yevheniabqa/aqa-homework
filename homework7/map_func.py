def my_map(callback, iterable):
    result = []

    for item in iterable:
        result.append(callback(item))

    return result
