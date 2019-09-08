example_string = input()

stats = list(map(int, example_string.split()))

print(f'В первый день посещений было столько: {stats[0]}, в третий день посещений было столько: {stats[2]}.')
