"""Computation of weighted average of squares."""

def average_of_squares(list_of_numbers, list_of_weights=None):
    """ Return the weighted average of a list of values.
    
    By default, all values are equally weighted, but this can be changed
    by the list_of_weights argument.
    
    Example:
    --------
    >>> average_of_squares([1, 2, 4])
    7.0
    >>> average_of_squares([2, 4], [1, 0.5])
    6.0
    >>> average_of_squares([1, 2, 4], [1, 0.5])
    Traceback (most recent call last):
    AssertionError: weights and numbers must have same length

    """
    squares = [i ** 2 for i in list_of_numbers]

    if list_of_weights is None:
        return sum(squares) / len(squares)

    assert len(list_of_weights) == len(list_of_numbers), "weights and numbers must have same length"
    weighted_squares = [a * b for a,b in zip(squares, list_of_weights)]
    return sum(weighted_squares) / len(weighted_squares)


def convert_numbers(list_of_strings):
    """Convert a list of strings into numbers, ignoring whitespace.
    
    Example:
    --------
    >>> convert_numbers(["4", " 8 ", "15 16", " 23    42 "])
    [4, 8, 15, 16, 23, 42]

    """
    all_numbers = []
    for s in list_of_strings:
        parts = [s1 for s1 in s.split()]
        for i in parts:
            all_numbers.append(int(i))

    return all_numbers


if __name__ == "__main__":
    numbers_strings = ["1","2","4"]
    weight_strings = ["1","1","1"]        
    
    numbers = convert_numbers(numbers_strings)
    weights = convert_numbers(weight_strings)
    
    result = average_of_squares(numbers, weights)
    
    print(result)