def insertion_sort(chaos_list):
    list_length = len(chaos_list)
    for main_index in range(1, list_length):
        current_element = chaos_list[main_index]
        sub_index = main_index - 1
        while sub_index >= 0 and current_element < chaos_list[sub_index]:
            chaos_list[sub_index + 1] = chaos_list[sub_index]
            sub_index -= 1
        chaos_list[sub_index + 1] = current_element
    return chaos_list
