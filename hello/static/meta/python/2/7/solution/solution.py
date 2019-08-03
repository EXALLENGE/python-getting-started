hour = int(input())


if 8 < hour < 13 or 14 < hour < 19:
    print('Kfc')
elif 9 < hour < 14 or 15 < hour < 17:
    print('Burger king')
elif 7 < hour < 20:
    print('mcDonalds')
else:
    print('все закрыто, сидите дома')
