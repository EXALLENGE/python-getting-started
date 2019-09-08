user_input = ''
articles = []

while user_input != 'STOP':
    user_input = input()
    splited_input = user_input.split()
    article_name = ' '.join(splited_input[:-1])
    article_name += ' ' * (16 - len(article_name))
    article = '|' + article_name + '|'
    article_stat = splited_input[-1]
    article_stat += ' ' * (6 - len(article_stat))

    article += article_stat + '|'
    articles.append(article)

print('+' * 25)

for article in articles[:-1]:
    print(article)

print('+' * 25)
