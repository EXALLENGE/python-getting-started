num_of_days = int(input())

num_of_articles = 0

schedule = [0, 1, 0, 0, 1, 1, 2]

for day in range(num_of_days):
    num_of_articles += schedule[(day % 7)]

print(num_of_articles)