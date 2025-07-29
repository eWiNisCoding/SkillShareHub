from django.contrib import admin
from .models import User, Profile, Course, Category, Enrollment

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_instructor', 'is_staff')
    list_filter = ('is_instructor', 'is_staff')
    search_fields = ('username', 'email')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'category', 'created_at')
    list_filter = ('category',)
    ordering = ('-created_at',)

admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Enrollment)
