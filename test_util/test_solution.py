import os
import sys
import json

import requests


def main(args):

    DOWNLOAD_URL = 'https://exallenge-programming.herokuapp.com'

    DOWNLOAD_URL = 'http://127.0.0.1:8000'

    if not os.path.exists(f'./{args[1]}'):
        print('Нет папки с главой')
        return

    if not os.path.exists(f'./{args[1]}/{args[2]}'):
        print('Нет папки с заданием')
        return

    if not os.path.isfile(f'./{args[1]}/{args[2]}/{args[3]}'):
        print('Нет файла с заданием')
        return

    r = requests.request(method='get',
                         url=f'{DOWNLOAD_URL}/task_from_util/',
                         data={'test_util_password': args[4], 'course_id': args[1],
                               'chapter_id': args[2], 'task_id': args[3]})

    if r.status_code != 200:
        print('Ошибка в запросе на сервер')
        return

    response = json.loads(r.text)
    print(response)



if __name__ == '__main__':
    args = sys.argv
    args = ['test_solution.py', '10', '1', '2', '123']
    main(args)

