from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

def login(request):
    return render(request, 'login.html')


def home(request):
    return render(request, 'home.html')


def courses(request):
    return render(request, 'courses.html')


def course(request, course_id):
    return render(request, 'course.html')


def task(request, task_id):
    return render(request, 'task.html')

@csrf_exempt
def create_course(request):
    data = request.POST
    return data


def create_chapter(request):
    data = request.POST
    return data


def create_task(request):
    data = request.POST
    return data

def content(request):
    return render(request, 'md.html', {'content':
        '# this is test title\n' +
        '- list 1\n' +
        '- list 2\n'
    })
