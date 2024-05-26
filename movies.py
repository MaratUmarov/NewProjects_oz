def is_film_exist(movie,films_list):
    for i_movie in films_list:
        if i_movie == movie:
            return True
    return False    

movies = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
          'Леон', 'Богемская рапсодия', 'Город грехов',
          'Мементо', 'Отступники', 'Деревня']
my_list=[]

while True:
    print('\nВаш текущий топ фильмов: ',my_list)
    new_movie=input('Название фильма: ')

    if is_film_exist(new_movie,movies):
        print('Команды: добавить, удалить, вставить')
        command=input('Введите команду: ')

        if command == 'добавить':
            my_list.append(new_movie)
         
        if command == 'удалить':
            if is_film_exist(new_movie,my_list):
                my_list.remove(new_movie)
            else:
                print('Такого фильма нет в нашем рейтинге.')
        if command == 'вставить':
            index = int(input('На какое место? '))
            my_list.insert(index - 1)        

    else:
        print('Такого фильма нет на сайте.')
    