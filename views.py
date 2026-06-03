from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Course, Question, Choice, Submission

def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        # Thu thập các ID của choice được chọn từ form
        selected_choice_ids = [int(value) for key, value in request.POST.items() if 'choice_' in key]
        
        # Tạo một submission mới
        submission = Submission.objects.create()
        for choice_id in selected_choice_ids:
            choice = get_object_or_404(Choice, pk=choice_id)
            submission.choices.add(choice)
        submission.save()
        
        return HttpResponseRedirect(reverse('onlinecourse:show_exam_result', args=(course.id, submission.id)))

def show_exam_result(request, course_id, submission_id):
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)
    
    # Tính điểm
    total_score = 0
    earned_score = 0
    
    # Lấy danh sách ID các câu trả lời mà user đã chọn
    selected_ids = [choice.id for choice in submission.choices.all()]
    
    for lesson in course.lesson_set.all():
        for question in lesson.question_set.all():
            total_score += question.grade
            if question.is_get_score(selected_ids):
                earned_score += question.grade
                
    # Giả định pass nếu đạt từ 80% trở lên
    is_passed = False
    if total_score > 0 and (earned_score / total_score) >= 0.8:
        is_passed = True
        
    context = {
        'course': course,
        'submission': submission,
        'total_score': total_score,
        'earned_score': earned_score,
        'is_passed': is_passed
    }
    return render(request, 'onlinecourse/exam_result.html', context)
