def coincidence(list=[], range=[]):
    if len(list) != 0 and len(range) != 0:
        min_number = min(range)
        max_number = max(range)
        result = []
        for i in list:
            if type(i) == int or type(i) == float:
                if min_number <= i <= max_number:
                    result.append(i)
        return result

    else:
        return list

print(coincidence([1, 2, 3, 4, 5], range(3, 6))) # => [3, 4, 5]
print(coincidence()) # => []
print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4))) # => [1, 2, 2.5]







