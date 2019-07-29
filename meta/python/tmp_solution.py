def __main_process_in_solution_which_we_are_going_to_test():
	hours_of_sleep = int(input())
	consumed_kilocalories = int(input())
	
	hours_of_sleep = max(hours_of_sleep-8, 0)
	
	consumed_kilocalories = (int(consumed_kilocalories / 100) + (consumed_kilocalories % 100 > 0))*100
	consumed_kilocalories = max(consumed_kilocalories-2600, 0)

	print(f'Вам нужно бегать {int(hours_of_sleep*10 + consumed_kilocalories/100*5)} минут.')
	print(f'Стоять в планке {hours_of_sleep*3} минут.')
	print(f'Отжаться {int(consumed_kilocalories/100*5)} раз.')
