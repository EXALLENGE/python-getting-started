example_string = input()

stats = list(map(int, example_string.split()))

print(stats)
for stat in stats[6::7]:
    print(stat)
