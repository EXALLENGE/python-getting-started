example_string = input()

stats = list(map(int, example_string.split()))

s = 0

for stat in stats:
    if stat > 1000:
        print(stat, end=' ')
