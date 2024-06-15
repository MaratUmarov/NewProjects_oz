import random

nums_1 = [
    29,
    17,
    10,
    15,
    13,
    22,
    12,
    22,
    7,
    24,
    26,
    3,
    11,
    2,
    3,
    16,
    19,
    21,
    2,
    3,
    8,
    27,
    2,
    17,
    2,
    20,
    12,
    21,
    3,
    1,
]

nums_2 = [
    16,
    21,
    30,
    24,
    5,
    7,
    23,
    13,
    11,
    5,
    21,
    5,
    19,
    9,
    12,
    9,
    15,
    16,
    29,
    8,
    16,
    1,
    22,
    15,
    16,
    9,
    1,
    13,
    21,
    21,
]

set_nums_1 = set(nums_1)
set_nums_2 = set(nums_2)
print(f"1-е множество: {set_nums_1}\n", f"2-е множество: {set_nums_2}")

del_s1 = min(set_nums_1)
del_s2 = min(set_nums_2)
print()
print(
    f"Минимальный элемент 1-го множества: {del_s1}\n",
    f"Минимальный элемент 2-го множества: {del_s2}",
)
print()
set_nums_1.discard(del_s1)
set_nums_2.discard(del_s2)

set_rand1 = random.randint(100, 200)
set_rand2 = random.randint(100, 200)
set_nums_1.add(set_rand1)
set_nums_2.add(set_rand2)
print(
    f"Случайное число для 1-го множества:{set_rand1}\n",
    f"Случайное число для 2-го множества:{set_rand2}",
)

print()
print(f"Объединение множеств: {set_nums_1|set_nums_2}\n")
print(f"Пересечение множеств: {set_nums_1&set_nums_2}\n")
print(f"Элементы, входящие в nums_2, но не входящие в nums_1:{set_nums_2-set_nums_1}")
print("\n------------------------------------")
