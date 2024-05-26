
favorite_movie = []
movies = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
          'Леон', 'Богемская рапсодия', 'Город грехов',
          'Мементо', 'Отступники', 'Деревня']
movie_amount = int(input('Сколько фильмов хотите добавить? '))

for _ in range(movie_amount):
    user_movie = input('Введите название фильма: ')


    if user_movie in movies:
        favorite_movie.append(user_movie)
    else:
        print(f'Ошибка: фильма {user_movie} у нас нет :(')
        
print(f'Ваш список любимых фильмов: {favorite_movie}')