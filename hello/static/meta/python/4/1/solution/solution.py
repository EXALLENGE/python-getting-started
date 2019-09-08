example_string = input()

stats = list(map(int, example_string.split()))

print('++++++++++++')

for stat in stats:
    len_of_num = len(str(stat))
    num_of_spaces = 10 - len_of_num
    print(f'|{stat}{" " * num_of_spaces}|')

print('++++++++++++')
