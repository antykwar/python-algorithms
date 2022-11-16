def selection_sort(chaos_list):
    for outer_index, outer_value in enumerate(chaos_list):
        min_value = outer_value
        min_key = outer_index
        for index in range(outer_index + 1, len(chaos_list)):
            value = chaos_list[index]
            if index <= outer_index:
                continue
            if value < min_value:
                min_value = value
                min_key = index
        chaos_list[outer_index], chaos_list[min_key] = min_value, outer_value
    return chaos_list
