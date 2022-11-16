def bubble_sort(chaos_list):
    for _ in range(len(chaos_list)):
        for index, value in enumerate(chaos_list):
            if index == len(chaos_list) - 1:
                continue
            if chaos_list[index] > chaos_list[index + 1]:
                chaos_list[index], chaos_list[index + 1] = chaos_list[index + 1], chaos_list[index]
    return chaos_list
