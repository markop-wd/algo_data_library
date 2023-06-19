def bubble_sort(value_list):
    value_list_length = len(value_list)
    for i in range(value_list_length):
        for j in range(value_list_length - i - 1):
            x = value_list[j]
            y = value_list[j + 1]
            if x > y:
                value_list[j], value_list[j + 1] = value_list[j + 1], value_list[j]

    return value_list

