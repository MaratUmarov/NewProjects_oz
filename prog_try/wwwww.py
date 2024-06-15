def parse_student_info(info):
    parts = info.split()
    student_info = {
        'Имя': parts[0],
        'Фамилия': parts[1],
        'Город': parts[2],
        'ВУЗ': parts[3],
        'Оценки': list(map(int, parts[-5:]))
    }
    return student_info


info = input("Введите информацию о студенте через пробел (имя, фамилия, город, место учёбы, оценки): ")
student_dict = parse_student_info(info)



for i_info in student_dict:
    print(i_info, '-',student_dict[i_info])