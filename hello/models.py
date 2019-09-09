from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    course_name = models.CharField(max_length=30)
    description = models.CharField(max_length=600)


class Chapter(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    chapter_name = models.CharField(max_length=100)
    chapter_number = models.IntegerField()


class Task(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=200)
    task_number = models.IntegerField(default=0)
    task_number_in_course = models.IntegerField(default=0)
    theory = models.TextField()
    need_program_check = models.BooleanField()
    need_teacher_check = models.BooleanField()

    # один вариант ответа, несколько вариантов ответа, открытый вопрос, развернутый ответ, код, нет задания
    NO_TASK = 'NT'
    ONE_CHOICE = 'OC'
    MULTIPLE_CHOICE = 'MC'
    OPEN_QUESTION = 'OQ'
    DETAILED_RESPONSE = 'DR'
    CODE = 'CD'
    TASK_TYPES = [
        (NO_TASK, 'no task'),
        (ONE_CHOICE, 'one choice'),
        (MULTIPLE_CHOICE, 'multiple choice'),
        (OPEN_QUESTION, 'open question'),
        (DETAILED_RESPONSE, 'detailed response'),
        (CODE, 'code')
    ]
    type_of_task = models.CharField(
        max_length=2,
        choices=TASK_TYPES,
        default=CODE,
    )


class TestCase(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    input_data = models.TextField()
    output_data = models.TextField()


class Flow(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    progress = models.IntegerField()


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    message_number = models.IntegerField()
    text = models.TextField()
