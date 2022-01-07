def max_odd(array):
        new_array = []
        for i in array:
            if type(i) == int or type(i) == float:
                if i % 2 != 0:
                    new_array.append(i)
        if len(new_array) != 0:
            result = max(new_array)
            return result
        else:
             return None

print(max_odd([1, 2, 3, 4, 4])) # => 3
print(max_odd([21.0, 2, 3, 4, 4])) # => 21
print(max_odd(['ololo', 2, 3, 4, [1, 2], None])) # => 3
print(max_odd(['ololo', 'fufufu'])) # => None
print(max_odd([2, 2, 4])) # => None