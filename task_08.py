def multiply_numbers(inputs=None):

    if inputs == None:                          #пустая строка
        return None

    elif isinstance(inputs, list):                      #если подается список
        inputs = int("".join([str(_) for _ in inputs]))
        mult = 1
        x = [int(a) for a in str(inputs)]
        for i in x:
            mult = mult * i
        return mult

    elif isinstance(inputs, float):  #дробная часть
        inputs = str(inputs)
        x = inputs.split('.')
        a = int(x[0])
        b = int(x[1])
        mult = 1
        while (a != 0):
            mult = mult * (a % 10)
            a = a // 10
        while (b != 0):
            mult = mult * (b % 10)
            b = b // 10
        return mult

    if isinstance(inputs, str):
        if inputs.isdigit() == True:            #состоит ли исходная строка только из цифровых символов
            mult = 1
            x = [int(a) for a in str(inputs)]
            for i in x:
                mult = mult * i
            return mult

        elif isinstance(inputs, str):  # состоит ли исходная строка только из буквенных символов
            if inputs.isalpha() == True:
                return None
            elif inputs.isalnum() == True:  # состоит ли исходная строка из буквенно-цифровых символов
                x = [a for a in str(inputs) if a in 'abcdefghijklmnopqrstuvxyz']
                z = [int(a) for a in str(inputs) if a in '1234567890']
                mult = 1
                for i in z:
                    mult = mult * i
                return mult


print(multiply_numbers()) # => None
print(multiply_numbers('ss')) # => None
print(multiply_numbers('1234')) # => 24
print(multiply_numbers('sssdd34')) # => 12
print(multiply_numbers(2.3)) # => 6
print(multiply_numbers([5, 6, 4])) # => 120