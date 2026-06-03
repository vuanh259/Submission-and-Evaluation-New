from django.contrib import admin
# Import đủ 7 classes cần thiết
from .models import Course, Lesson, Question, Choice, Submission

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    fields = ['lesson', 'question_text', 'grade']
    inlines = [ChoiceInline]
    list_display = ['question_text', 'lesson', 'grade']

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [QuestionInline]

# Đăng ký các admin class còn lại để hiển thị đầy đủ trong trang admin
admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
