def create_dict(num,expon):
    return {i: i**expon for i in range(1, num + 1)}


# Пример использования функции
num = int(input('enter num: '))
expon_num=int(input('enter rising num to a power: '))



squared_dict = create_dict(num,expon_num)
print(squared_dict)

