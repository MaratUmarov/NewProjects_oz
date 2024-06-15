def find_rotation_point(str1, str2):
    if len(str1) != len(str2):
        return -1  # Строки разной длины, сдвиг невозможен

    # Объединяем вторую строку с самой собой, чтобы учесть циклический сдвиг
    temp = str2 + str2

    # Проверяем, содержится ли первая строка в объединенной второй строке
    if str1 in temp:
        return temp.index(str1)  # Возвращаем индекс начала первой строки в объединенной второй строке
    else:
        return -1  # Первая строка не может быть получена циклическим сдвигом второй строки

# Пример использования функции
str1 = "abcd"
str2 = "cdba"
rotation_point = find_rotation_point(str1, str2)

if rotation_point != -1:
    print(f"Первую строку можно получить из второй циклическим сдвигом на {rotation_point} позиций.")
else:
    print("Первую строку нельзя получить из второй циклическим сдвигом.")
