# Как устроен цикл for?

Что может быть хуже, чем повторять одно и то же действие снова и снова? У нас уже было много задач где мы делали достаточно много монотонной работы. Наша задача делать меньше действий чем компьютер, а не наоборот. Для этого в программировании придумали специальную конструкцию. Эта конструкция называется `for` и она повторяет куски кода нужное число раз.

Представьте, что у нас есть список и мы хотим вывести каждый его элемент.

Как это выглядит без циклов:

```
l = [1, 2, 3]
print(l[0])
print(l[1])
print(l[2])
```

Не очень удобно, потому что этот код сработает только для списка с тремя элементами.

Вот как можно написать этот код с использованием цикла for:

```
l = [1, 2, 3]
for item in l:
	print(item)
```

Этот код можно прочитать так: для каждого элемента из листа выполни команду print.

Задание:

На вход приходит строка с положительными числами не больше 10000 через пробел.

Ваша задача вывести элементы в формате:

```
++++++++++++
| 234      |
| 12       |
| 1245     |
++++++++++++
```

Подсказка:
1. В каждой строке должно быть по 12 символов.