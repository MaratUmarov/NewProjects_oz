user_str = set(input("Введите строку: "))
numbers_set = set("0,1,2,3,4,5,6,7,8,9")
diff = (numbers_set & user_str)
diff_str=''
for i in diff:
    diff_str+=i


print(f"Различные цифры строки: {diff_str}")
