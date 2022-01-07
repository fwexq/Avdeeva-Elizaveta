def sort_list(list):
    if len(list) > 0:
        max_number, min_number = max(list), min(list)
        for i in range(len(list)):
            if list[i] == min_number:
                list[i] = max_number
            elif list[i] == max_number:
                list[i] = min_number
        list.append(min_number)
        return list

    else:
        return list

print(sort_list([])) # => []
print(sort_list([2, 4, 6, 8])) # => [8, 4, 6, 2, 2]
print(sort_list([1])) # => [1, 1]
print(sort_list([1, 2, 1, 3])) # => [3, 2, 3, 1, 1]
