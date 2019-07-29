import os


user_submit = open('solution.py', 'r')
tmp_file = open('_tmp_solution.py', 'w')

tmp_file.write('def __main_process_in_solution_which_we_are_going_to_test():\n')
for line in user_submit:
    tmp_file.write(f'\t{line}')
user_submit.close()
tmp_file.close()

# create file test_solution, folder test_cases (download or read from cache)

os.system('python test_solution.py')

# output report

# delete _tmp_solution.py, test_solution.py, test_cases, report.txt
