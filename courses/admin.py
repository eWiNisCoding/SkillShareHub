from django.contrib import admin
from .models import User, Profile, Category, Course, Enrollment

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_instructor', 'is_student')

admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Enrollment)