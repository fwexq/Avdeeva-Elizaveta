def connect_dicts(dict1, dict2):
    merge = {}
    summa_dict1 = sum(dict1.values())
    summa_dict2 = sum(dict2.values())
    if summa_dict1 > summa_dict2:
        dict2.update(dict1)
        merge = dict2.copy()
    elif summa_dict2 > summa_dict1:
        dict1.update(dict2)
        merge = dict1.copy()
    if summa_dict1 == summa_dict2:
        dict1.update(dict2)
        merge = dict1.copy()
    result = {}
    for key, value in (merge.items()):
        if value > 9:
            result[key] = value
    sorted_tuples = sorted(result.items(), key=lambda item: item[1])
    sorted_dict = dict(sorted_tuples)
    return sorted_dict

print(connect_dicts({ "a": 2, "b": 12 }, { "c": 11, "e": 5 })) # => { "c": 11, "b": 12 }
print(connect_dicts({ "a": 13, "b": 9, "d": 11 }, { "c": 12, "a": 15 })) # => { d: 11, "c": 12, "a": 13 }
print(connect_dicts({ "a": 14, "b": 12 }, { "c": 11, "a": 15 })) # => { "c": 11, "b": 12, "a": 15 }

