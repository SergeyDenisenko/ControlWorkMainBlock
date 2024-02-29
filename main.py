# Ввод строки разделенной пробелом
# разбиение строки на массив строк

max_char = 3
new_arr = [item for item in input("Введите строку: ").split() if len(item) <= max_char]

print(new_arr)