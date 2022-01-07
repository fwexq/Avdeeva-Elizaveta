from collections import Counter
def count_words(string):
        string = string.replace(',', '').replace('-- ', '').lower().split(' ')
        return dict(Counter(string))

print(count_words("A man, a plan, a canal -- Panama")) # => {"a": 3, "man": 1,"canal": 1, "panama": 1, "plan": 1}
print(count_words("Doo bee doo bee doo")) # => {"doo": 3, "bee": 2}


