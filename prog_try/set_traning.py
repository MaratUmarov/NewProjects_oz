import random

numbers_list=[random.randint(1,4) for _ in range(10)]
new_list=[]

for i_num in numbers_list:
    if i_num not in new_list:
        new_list.append(i_num)
print(numbers_list)
print(new_list)

unique = set(numbers_list)
print(unique)