import os
import sys
import json

import requests


def main(args):

    DOWNLOAD_URL = 'https://exallenge-programming.herokuapp.com'

    DOWNLOAD_URL = 'http://127.0.0.1:8000'

    if not os.path.exists(f'./{args[2]}'):
        print('Нет папки с главой')
        return

    if not os.path.exists(f'./{args[2]}/{args[3]}'):
        print('Нет папки с заданием')
        return

    if not os.path.isfile(f'./{args[2]}/{args[3]}/solution.py'):
        print('Нет файла с заданием')
        return

    user_submit = open(f'./{args[2]}/{args[3]}/solution.py', 'r')
    tmp_file = open(f'./tmp_solution.py', 'w')

    tmp_file.write('def __main_process_in_solution_which_we_are_going_to_test():\n')
    for line in user_submit:
        tmp_file.write(f'\t{line}')
    user_submit.close()
    tmp_file.close()

    import tmp_solution
    print(tmp_solution)

    r = requests.request(method='get',
                         url=f'{DOWNLOAD_URL}/task_from_util/',
                         data={'test_util_password': args[4], 'course_id': args[1],
                               'chapter_id': args[2], 'task_id': args[3]})

    if r.status_code != 200:
        print('Ошибка в запросе на сервер')
        return

    response = json.loads(r.text)
    print(response)

    for test in response:
        input_data = [line.rstrip('\n') for line in test['input_data'].split('\n')]
        output_data = [line.rstrip('\n') for line in test['output_data'].split('\n')]
        program_result = []

        tmp_solution.input = lambda: input_data.pop(0)
        tmp_solution.print = lambda s: program_result.append(s)

        try:
            tmp_solution.__main_process_in_solution_which_we_are_going_to_test()
        except Exception as e:
            print(f'{e}\n')
            break

        if len(program_result) == len(output_data) and all(a == b for a, b in zip(program_result, output_data)):
            print('OK\n')
            r = requests.request(method='post',
                                url=f'{DOWNLOAD_URL}/task_from_util/',
                                data={'test_util_password': args[4], 'course_id': args[1],
                                    'chapter_id': args[2], 'task_id': args[3]})
        else:
            print('Wrong answer\n')
            break

    os.remove('./tmp_solution.py')


if __name__ == '__main__':
    args = sys.argv
    args = ['test_solution.py', '10', '1', '2', '123']
    main(args)

