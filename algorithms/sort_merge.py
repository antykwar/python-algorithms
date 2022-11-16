def merge_sort(chaos_list):
    if len(chaos_list) <= 1:
        return chaos_list

    list_1 = merge_sort(chaos_list[:len(chaos_list) // 2])
    list_2 = merge_sort(chaos_list[len(chaos_list) // 2:])

    merged_list = []
    left_index = right_index = 0

    while left_index < len(list_1) or right_index < len(list_2):
        if left_index >= len(list_1):
            merged_list.append(list_2[right_index])
            right_index += 1
        elif right_index >= len(list_2):
            merged_list.append(list_1[left_index])
            left_index += 1
        else:
            if list_1[left_index] <= list_2[right_index]:
                merged_list.append(list_1[left_index])
                left_index += 1
            else:
                merged_list.append(list_2[right_index])
                right_index += 1

    return merged_list
