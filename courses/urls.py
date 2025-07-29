from django.urls import path
from .views import register_view, login_view, logout_view, CourseListView, CourseCreateView, CourseUpdateView, CourseDeleteView

urlpatterns = [
    path('', CourseListView.as_view(), name='course_list'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('course/create/', CourseCreateView.as_view(), name='course_create'),
    path('course/<int:pk>/edit/', CourseUpdateView.as_view(), name='course_edit'),
    path('course/<int:pk>/delete/', CourseDeleteView.as_view(), name='course_delete'),
]
