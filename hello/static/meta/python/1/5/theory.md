# Переменные

Мы уже давольно много знаем, но еще пока не умеем писать реально полезные программы. Почти всегда данные меняются в нашей жизни. Скорость, координаты, время и т. д. И эти данные нужно где-то хранить.Для это придумали такую вещь как переменные!(Да-да, программисты очень оригинальные). Переменные нам нужны, чтобы сохранить данные для их дальнейшей обработки. Python выбирает место в памяти куда можно сохранить эти данные, и чтобы к этим данным можно было обращаться мы должны дать им имя. Работает это так:

```
my_first_var = 12
```

Теперь мы можем что-то делать с этой пересенной. Например напечатать ее:

```
print(my_first_var)
```

Задание: 

Вы собрались в путешествие! Вы едете в Америку, и вы уже знаете сколько потратите в каждом городе в долларах. Ваша задача понять сколько вы потратите на всю поездку в рублях. 

Вы поситите 3 города(Вашингтон, Нью-йорк, Филадельфия). В первом вы потратите 12 долларов, во втором 16 и в третьем 14. Курс доллара к рублю на тот момент был 64 рубля за 1 доллар.

Ваша задача вывести ответ в виде: 'На всю поздку будет потрачено <сумма> р.'

Подсказка:

1. Вместо конкатенации гораздо легче использовать f-strings. 
В этом случае вам просто нужно написать:
```
 print(f'На всю поздку будет потрачено {переменная} р.') 
```