import os
import shutil


user_submit = open('solution.py', 'r')
tmp_file = open('tmp_solution.py', 'w')

tmp_file.write('def __main_process_in_solution_which_we_are_going_to_test():\n')
for line in user_submit:
    tmp_file.write(f'\t{line}')
user_submit.close()
tmp_file.close()

# create file test_solution, folder test_cases (download or read from cache)

os.system('python test_solution.py')

# output report
report = open('report.txt', 'r')
num_of_tests = report.readline()


# delete tmp_solution.py, test_solution.py, test_cases, report.txt
os.remove('tmp_solution.py')
os.remove('test_solution.py')
os.remove('report.txt')
shutil.rmtree('test_cases')