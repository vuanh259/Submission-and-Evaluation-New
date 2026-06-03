from django.contrib import admin
# IMPORT ĐỦ 7 CLASSES THEO YÊU CẦU CỦA RUBRIC
from .models import Course, Lesson, Question, Choice, Submission, Instructor, Learner

# 1. Triển khai ChoiceInline
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

# 2. Triển khai QuestionInline
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1

# 3. Triển khai QuestionAdmin
class QuestionAdmin(admin.ModelAdmin):
    fields = ['lesson', 'question_text', 'grade']
    inlines = [ChoiceInline]
    list_display = ['question_text', 'lesson', 'grade']

# 4. Triển khai LessonAdmin
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [QuestionInline]

# Đăng ký hiển thị các model còn lại trong Admin Site
admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
admin.site.register(Instructor)
admin.site.register(Learner)
