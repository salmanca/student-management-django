from django.urls import path
from . import views

urlpatterns = [
    path('add-student/', views.add_student, name='add_student'),
    path('edit-student/<int:student_id>/', views.edit_student, name='edit_student'),
    path('view-student/<int:student_id>/', views.view_student, name='view_student'),
    path('delete-student/', views.delete_student, name='delete_student'),
]
