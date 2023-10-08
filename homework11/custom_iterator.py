class CustomIterator:
    def __init__(self, sequence, start_index, end_index):
        self.sequence = sequence
        self.start_index = start_index
        self.end_index = end_index

    def __iter__(self):
        return self

    def __next__(self):
        if self.start_index <= self.end_index:
            current_index = self.start_index
            self.start_index += 1
            return self.sequence[current_index]
        else:
            raise StopIteration

"""# Example usage of CustomIterator
sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
iterator = CustomIterator(sequence, 2, 7)
for value in iterator:
    print(value)"""
