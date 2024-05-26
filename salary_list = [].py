salary_list = []
employee = int(input('Введите кол-во сотрудников: '))


print('Кол-во сотрудников ',employee)


for i_imp in range(employee):
    salary = int(input('Введите зп сотрудника: '))
    salary_list.append(salary)
    
for k in range(len(salary_list)):
    print(f'Зарплата {k+1} сотрудника:{salary_list[k]}' )
print(salary_list)  

for i in range(len(salary_list)):
    if salary_list[i]==0 :
        
        salary_list.remove(0)
    
print(salary_list)      
