# цикл while

Отлично! Мы уже разобрались с циклом for. Это очень удобный цикл когда мы заранее знаем сколько у нас элементов, когда мы идем по массиву или по строке. 

Но в нашей жизни очень часто бывает такое, когда мы не знаем  заранее количество повторений. Например, наши задания: делай, пока он не будет сделано полностью.

В таких случаях, когда цикл повторяется снова и снова, пока не выполнится условие, используют цикл while. Вот его пример:

```
i = 0

while i != 10:
	i = int(input())
	print('Вы ввели {i}')

```

Этот цикл будет работать пока пользователь не введет число 10.

Задание:

Цикл while очень удобно использовать при работе с пользовательским вводом. 

На вход программе поступают строки которые состоят из названия статьи и числа просмотров. Последняя строка содержит слово "STOP", она означет конец последовательности.

Все строки записаны в формате: "Первая статья в блоге 3000" (Название и число просмотров через пробел).

Ваша задача вывести названия всех статей и сумму просмотров в формате:

```
+++++++++++++++++++++++++
|Первая статья   |3021  |
|Вторая статья   |211   |
+++++++++++++++++++++++++
```

Подсказка:

Первая колонка должна быть 16 символов в длину, а вторая 6.