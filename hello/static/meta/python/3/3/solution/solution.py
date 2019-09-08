example_string = input()

stats = list(map(int, example_string.split()))

# так можно получить сумму элементов массива
sum_of_elements = sum(stats)


# так можно получить длинну массива
len_of_array = len(stats)

print(sum_of_elements/len_of_array)


