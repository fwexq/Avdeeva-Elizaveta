def combine_anagrams(words_array):
    if isinstance(words_array, list):
        new_anagrams = []
        for i in words_array:
            ana = []
            for alt in words_array:
                if sorted(i) == sorted(alt):
                    ana.append(alt)

            if ana not in new_anagrams:
                new_anagrams.append(ana)

        return new_anagrams


print(combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar", "creams", "scream"])) # => [ ["cars", "racs", "scar"], ["four"], ["for"],["potatoes"], ["creams", "scream"] ]