def get_array_strings(max_char):
    return [item for item in input("Введите строку: ").split() if len(item) <= max_char]

# print(get_array_strings(3))