def fibonacci_recursive(number):
    if number < 0 or type(number) != int:
        raise ValueError('Factorial function gets only non-negative whole numbers')
    if number < 2:
        return number
    return fibonacci_recursive(number - 1) + fibonacci_recursive(number - 2)


def fibonacci_recursive_dynamic():
    internal_cache = {}

    def fibonacci_recursive_closure(number):
        if number < 0 or type(number) != int:
            raise ValueError('Factorial function gets only non-negative whole numbers')
        if number in internal_cache:
            return internal_cache[number]
        if number < 2:
            return number
        internal_cache[number] = fibonacci_recursive_closure(number - 1) + fibonacci_recursive_closure(number - 2)
        return internal_cache[number]

    return fibonacci_recursive_closure


a = fibonacci_recursive_dynamic()
print(a(7))
