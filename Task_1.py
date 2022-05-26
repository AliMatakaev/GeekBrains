duration = int(input('Введите время в секундах '))
# Минута = 60 секунд, час = 3600 секунд, день = 86400 секунд.
day = duration // 86400
hour = duration % 86400 // 3600
min = duration % 86400 % 3600 // 60
sec = duration % 86400 % 3600 % 60

if day > 0:
    print(f'{day} дн {hour} час {min} мин {sec} сек')
elif hour > 0:
    print(f'{hour} час {min} мин {sec} сек')
elif min > 0:
    print(f'{min} мин {sec} сек')
elif sec < 60:
    print(duration, 'сек')