from django.urls import path
from .views import (
    register_view,
    login_view,
    logout_view,
    CourseListView,
    CourseCreateView
)

urlpatterns = [
    path('', CourseListView.as_view(), name='course_list'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('create/', CourseCreateView.as_view(), name='course_create'),
]