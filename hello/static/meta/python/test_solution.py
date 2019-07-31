import tmp_solution

import os
tests = os.listdir('test_cases')

f = open('report.txt', 'w')
f.write(f'{len(tests)}\n')

for test in tests:
    input_data = [line.rstrip('\n') for line in open(f'./test_cases/{test}/input.txt')]
    output_data = [line.rstrip('\n') for line in open(f'./test_cases/{test}/output.txt')]
    program_result = []

    tmp_solution.input = lambda  : input_data.pop(0)
    tmp_solution.print = lambda s: program_result.append(s)

    try:
        tmp_solution.__main_process_in_solution_which_we_are_going_to_test()
    except Exception as e:
        f.write(f'{e}\n')
        break

    if len(program_result) == len(output_data) and all(a==b for a, b in zip(program_result, output_data)):
        f.write('OK\n')
    else:
        f.write('Wrong answer\n')
        break
