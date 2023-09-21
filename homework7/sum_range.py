def sum_of_range(start, end):
    if start > end:
        start, end = end, start

    total_sum = 0

    for num in range(start, end + 1):
        total_sum += num

    return total_sum

