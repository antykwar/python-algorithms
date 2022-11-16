def reverse_string(initial_string):
    if len(initial_string) == 0:
        return initial_string
    return initial_string[-1] + reverse_string(initial_string[:len(initial_string) - 1])
