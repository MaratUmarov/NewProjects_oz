punct_marks = set(".,;:!?")
user_string = input("Введите строку: ")

marks = punct_marks.intersection(user_string)

count_marks = len(marks)

print(f"Количество знаков пунктуации: {count_marks}")
