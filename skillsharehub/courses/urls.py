from django.urls import path
from .views import register_view, login_view, logout_view, CourseListView

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', CourseListView.as_view(), name='course_list'),
]
