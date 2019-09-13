import random
import string
import datetime

from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseNotAllowed
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from .models import Course, Chapter, Task, TestCase, Flow, UserInfo


def login(request):
    return render(request, 'login.html')


def home(request):
    return render(request, 'home.html')


def courses(request):
    user = request.user
    if not request.user:
        user = None
    courses = Course.objects.all()
    for course in courses:
        try:
            flow = Flow.objects.get(course=course, user=user)
        except Flow.DoesNotExist:
            flow = None
        course.flow = flow
    return render(request, 'courses.html', {'courses': courses})


def reviews(request):
    return render(request, 'reviews.html')


def feedback(request):
    return render(request, 'feedback.html')


def course(request, course_id):
    user = request.user
    if not request.user:
        user = None

    course = Course.objects.get(pk=course_id)
    chapters = Chapter.objects.filter(course=course)
    for chapter in chapters:
        tasks = Task.objects.filter(chapter=chapter).order_by('task_number')
        chapter.tasks = tasks

    try:
        flow = Flow.objects.get(course=course, user=user)
    except Flow.DoesNotExist:
        flow = None

    if flow:
        user_progress = flow.progress - 1
        for chapter in chapters:
            if not user_progress:
                break
            for task in chapter.tasks:
                if not user_progress:
                    break
                task.made = True
                user_progress -= 1

    return render(request, 'course.html', {'chapters': chapters, 'course': course})


@login_required
def task(request, course_id, chapter_id, task_id):
    user = request.user
    course = Course.objects.get(pk=course_id)
    chapter = Chapter.objects.get(course=course, chapter_number=chapter_id)
    task = Task.objects.get(chapter=chapter, task_number=task_id)
    try:
        flow = Flow.objects.get(course=course, user=user)
    except Flow.DoesNotExist:
        return redirect(f'/course/{course.id}')

    # получаем номер задания
    task_number = 0

    chapters = Chapter.objects.filter(course=course, chapter_number__in=list((i for i in range(chapter_id-1))))

    for ch in chapters:
        task_number += len(Task.objects.filter(chapter=ch))

    task_number += task_id

    if task_number > flow.progress:
        return redirect(f'/course/{course.id}')

    return render(request, 'task.html', {'content': task.theory})


@login_required
def user_page(request):
    user = request.user

    letters = string.ascii_lowercase
    try:
        user_info = UserInfo.objects.get(user=user)
    except UserInfo.DoesNotExist:
        user_info = UserInfo(user=user, test_util_password=''.join(random.choice(letters) for i in range(10)))
        user_info.save()

    flows = Flow.objects.filter(user=user).select_related('course')
    return render(request, 'user-page.html', {'flows': flows, 'user_info': user_info})


@login_required
def start_course(request, course_id):
    user = request.user
    course = Course.objects.get(pk=course_id)
    flow = Flow(user=user, course=course, start_date=datetime.datetime.now(), progress=1)
    flow.save()
    return redirect(f'/course/{course_id}/')


@csrf_exempt
def create_course(request):
    data = request.POST
    course = Course(course_name=data['course_name'], description=data['description'])
    course.save()
    return JsonResponse({'course_id': course.id})


@csrf_exempt
def create_chapter(request):
    data = request.POST
    course = Course.objects.get(pk=data['course_id'])
    chapter = Chapter(course=course, chapter_name=data['chapter_name'], chapter_number=data['chapter_number'])
    chapter.save()
    return JsonResponse({'chapter_id': chapter.id})


@csrf_exempt
def task_from_util(request):
    if request.method == 'GET':
        body_unicode = request.body.decode('utf-8')
        data = {i.split('=')[0]: i.split('=')[1] for i in body_unicode.split('&')}

        try:
            course_id = int(data['course_id'])
            chapter_id = int(data['chapter_id'])
            task_id = int(data['task_id'])

            user_info = UserInfo.objects.get(test_util_password=data['test_util_password'])
            user = user_info.user
            flow = Flow.objects.get(user=user)

            course = Course.objects.get(pk=course_id)
            chapter = Chapter.objects.get(course=course, chapter_number=chapter_id)
            task = Task.objects.get(chapter=chapter, task_number=task_id)
        except Exception as e:
            return JsonResponse({'status': 'NO', 'message': 'Проверьте аргументы для скрипта'})

        # получаем номер задания
        task_number = 0

        chapters = Chapter.objects.filter(course=course, chapter_number__in=list((i for i in range(chapter_id-1))))

        for ch in chapters:
            task_number += len(Task.objects.filter(chapter=ch))

        task_number += task_id

        if task_number > flow.progress:
            return JsonResponse({'status': 'NO', 'message': 'Нет доступа к этому заданию'})

        test_cases = TestCase.objects.filter(task=task)
        return JsonResponse([{'input_data': test_case.input_data, 'output_data': test_case.output_data}
                             for test_case in test_cases], safe=False)

    elif request.method == 'POST':
        pass
    return HttpResponseNotAllowed(['POST', 'GET'])



@csrf_exempt
def create_task(request):
    data = request.POST
    chapter = Chapter.objects.get(pk=data['chapter_id'])
    task = Task(chapter=chapter,
                task_name=data['task_name'],
                need_program_check=data['need_program_check'],
                need_teacher_check=data['need_teacher_check'],
                task_number=data['task_number'],
                task_number_in_course=data['task_number_in_course'],
                theory=data['theory'],
                type_of_task=data['task_type'])
    task.save()
    return JsonResponse({'task_id': task.id})


@csrf_exempt
def create_test(request):
    data = request.POST
    task = Task.objects.get(pk=data['task_id'])
    test_case = TestCase(task=task,
                input_data=data['input_data'],
                output_data=data['output_data'])
    test_case.save()
    return JsonResponse({'task_id': task.id})


def content(request):
    return render(request, 'md.html', {'content':
        '# this is test title\n' +
        '- list 1\n' +
        '- list 2\n'
    })
