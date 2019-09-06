import os
import json

import requests


token = 'qwe123rty456'

URL = 'http://127.0.0.1:8000'
COURSE_PATH = '../hello/static/meta/python/'


def save_test_cases(task_id, task_path):
    if not os.path.exists(f'{task_path}/test_cases'):
        return
    for test in os.listdir(f'{task_path}/test_cases'):
        if os.path.isdir(f'{COURSE_PATH}{folder}/{task}') and not folder.startswith('_'):
            input = open(f'{task_path}/test_cases/{test}/input.txt', 'r').read()
            output = open(f'{task_path}/test_cases/{test}/output.txt', 'r').read()
            test_info = {'task_id': task_id, 'input_data': input, 'output_data': output}
            r = requests.post(f'{URL}/create_test/', data=test_info)
            print(r.text)


with open(f'{COURSE_PATH}meta.json') as json_file:
    data = json.load(json_file)
    r = requests.post(f'{URL}/create_course/', data=data)
    print(r.text)
    res = json.loads(r.text)
    course_id = res['course_id']
    for folder in os.listdir(COURSE_PATH):
        if os.path.isdir(f'{COURSE_PATH}{folder}') and not folder.startswith('_'):
            with open(f'{COURSE_PATH}{folder}/meta.json') as chapter_file:
                chapter_info = json.load(chapter_file)
                chapter_info.update({'course_id': course_id, 'chapter_number': folder})
                r = requests.post(f'{URL}/create_chapter/', data=chapter_info)
                print(r.text)
                chapter_id = json.loads(r.text)['chapter_id']
                for task in os.listdir(f'{COURSE_PATH}{folder}'):
                    if os.path.isdir(f'{COURSE_PATH}{folder}/{task}') and not task.startswith('_'):
                        with open(f'{COURSE_PATH}{folder}/{task}/meta.json') as task_file:
                            task_info = json.load(task_file)
                            task_theory = open(f'{COURSE_PATH}{folder}/{task}/theory.md', 'r').read()
                            task_info.update({'chapter_id': chapter_id, 'task_number': task, 'theory': task_theory})
                            r = requests.post(f'{URL}/create_task/', data=task_info)
                            print(r.text)
                            task_id = json.loads(r.text)['task_id']
                            save_test_cases(task_id, f'{COURSE_PATH}{folder}/{task}')
