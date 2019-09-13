from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from hello import views

admin.autodiscover()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('social-auth/', include('social_django.urls', namespace="social")),

    path("login/", views.login, name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("reviews/", views.reviews, name="reviews"),
    path("feedback/", views.feedback, name="reviews"),
    path("user-page/", views.user_page, name="user-page"),
    path('md/', views.content, name='md'),

    path('', views.home, name="home"),
    path('courses/', views.courses, name='courses'),
    path('start_course/<int:course_id>/', views.start_course, name='start_course'),
    path('course/<int:course_id>/', views.course, name='course'),
    path('task/<int:course_id>/<int:chapter_id>/<int:task_id>/', views.task, name='task'),

    path('task_from_util/', views.task_from_util, name='task_from_util'),
    path('create_course/', views.create_course, name='create_course'),
    path('create_chapter/', views.create_chapter, name='create_chapter'),
    path('create_task/', views.create_task, name='create_task'),
    path('create_test/', views.create_test, name='create_test'),
]