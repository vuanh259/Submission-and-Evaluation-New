from django.db import models
from django.utils import timezone

# Giả định bạn đã có model Course và Lesson trước đó
class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name

class Lesson(models.Model):
    title = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

# --- CÁC MODEL THEO YÊU CẦU ---

class Question(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=500)
    grade = models.IntegerField(default=1)

    def __str__(self):
        return self.question_text

    def is_get_score(self, selected_ids):
        all_answers = self.choice_set.filter(is_correct=True).count()
        selected_correct = self.choice_set.filter(is_correct=True, id__in=selected_ids).count()
        selected_wrong = self.choice_set.filter(is_correct=False, id__in=selected_ids).count()
        
        if all_answers == selected_correct and selected_wrong == 0:
            return True
        return False

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=500)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text

class Submission(models.Model):
    enrollment = models.ForeignKey('Enrollment', on_delete=models.CASCADE, null=True, blank=True) # Thay đổi tùy thuộc vào hệ thống user/enrollment của bạn
    choices = models.ManyToManyField(Choice)
    date_submitted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Submission {self.id} at {self.date_submitted}"
