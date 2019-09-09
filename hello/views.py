import datetime

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from .models import Course, Chapter, Task, TestCase, Flow


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
        tasks = Task.objects.filter(chapter=chapter)
        chapter.tasks = tasks

    try:
        flow = Flow.objects.get(course=course, user=user)
    except Flow.DoesNotExist:
        flow = None

    if flow:
        user_progress = flow.progress
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
def task(request, task_id):
    return render(request, 'task.html')


@login_required
def user_page(request):
    print(request)
    return render(request, 'user-page.html')


@login_required
def start_course(request, course_id):
    user = request.user
    course = Course.objects.get(pk=course_id)
    flow = Flow(user=user, course=course, start_date=datetime.datetime.now(), progress=0)
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
