from django.urls import path
from . import views

app_name = 'onlinecourse'
urlpatterns = [
    # ... Các đường dẫn cũ của bạn (ví dụ: course_details) ...
    
    # Thêm 2 đường dẫn theo yêu cầu task 6:
    path('course/<int:course_id>/submit/', views.submit, name='submit'),
    path('course/<int:course_id>/submission/<int:submission_id>/result/', views.show_exam_result, name='show_exam_result'),
]
