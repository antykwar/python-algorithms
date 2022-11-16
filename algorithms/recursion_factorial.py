def factorial_recursive(number):
    if number < 0 or type(number) != int:
        raise ValueError('Factorial function gets only non-negative whole numbers')
    if number < 2:
        return 1
    return number * factorial_recursive(number - 1)
