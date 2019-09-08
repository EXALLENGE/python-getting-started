example_string = input()

stats = list(map(int, example_string.split()))

counter = 0

for stat in stats:
    if counter > 2:
        break
    if stat < 10000:
        print(stat, end=' ')
        counter += 1
