def is_palindrome(text):
    text = str(text)
    symbol = [" ",".", ",", "-","!", "?", "'"]
    for i in symbol:
        text = text.replace(i, '')
    text = text.lower()
    return text == text[::-1]

print(is_palindrome("A man, a plan, a canal -- Panama")) # => True
print(is_palindrome("Madam, I'm Adam!")) # => True
print(is_palindrome(333)) # => True
print(is_palindrome(None)) # => False
print(is_palindrome("Abracadabra")) # => False