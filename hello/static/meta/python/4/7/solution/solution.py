counter = 0

while True:
    print('Сколько будет 8 * 5')
    answer = input()
    if answer != '40':
        counter += 1
    if answer == '40' or counter == 3:
        break
