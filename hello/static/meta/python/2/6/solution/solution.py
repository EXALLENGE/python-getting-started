available_commands = input()
budget = int(input())
no_debt = input()


if available_commands == 'да' and budget > 15000 and no_debt == 'да':
    print('Проект можно взять как срочный')
else:
    print('Проект нельзя взять как срочный')
