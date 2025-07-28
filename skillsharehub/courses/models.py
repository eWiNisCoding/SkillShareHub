from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    is_instructor = models.BooleanField(default=False)
    is_student = models.BooleanField(default=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

class Category(models.Model):
    name = models.CharField(max_length=100)

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(default=timezone.now)

class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(default=timezone.now)
