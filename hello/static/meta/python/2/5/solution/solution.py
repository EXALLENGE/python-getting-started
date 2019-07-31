name = input()
day_of_week = int(input())

if name == '':
    print('Не указано имя')
else:
    if (day_of_week % 2) == 0:
        print('нужно спросить про отчет')
    else:
        print('сегодня отчет не нужен')