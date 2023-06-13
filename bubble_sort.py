def sort(value_list):
    value_list_length = len(value_list)
    for run in range(value_list_length):
        for x_pos in range(value_list_length - run - 1):
            x = value_list[x_pos]
            y = value_list[x_pos + 1]
            if x > y:
                value_list[x_pos], value_list[x_pos + 1] = value_list[x_pos + 1], value_list[x_pos]

    return value_list
