from django.shortcuts import render, redirect
from .models import StudentModel, SubjectsModel
from django.contrib.auth.decorators import login_required

# To view all the student list in loged in user
@login_required(login_url = 'login')
def view_student(request, student_id):
    student = StudentModel.objects.get(id = student_id)
    subjects = SubjectsModel.objects.filter(student=student.id)
    context = {
        "student" : student,
        "subjects" : subjects
    }
    return render(request, 'students/detail_page.html', context)

# To edit specific student and there subjects
@login_required(login_url = 'login')
def edit_student(request, student_id):
    if request.method == "POST":
        subject = request.POST['subject']
        marks = request.POST['marks']
        subject_id = request.POST['id']
        subject_model = SubjectsModel.objects.get(id = int(subject_id))
        subject_model.subject = subject
        subject_model.marks = marks
        subject_model.save()
    return redirect(view_student, student_id)

# Deleting the student and there subjects
@login_required(login_url = 'login')
def delete_student(request):
    if request.method == "POST":
        try:
            student_id = request.POST['student_id']
        except:
            student_id = None
        
        try:
            subject_id = request.POST['subject_id']
        except:
            subject_id = None

        if student_id:
            student = StudentModel.objects.get(id = int(student_id)).delete()
        elif subject_id:
            subject = SubjectsModel.objects.get(id = int(subject_id)).delete()
        return redirect('dashboard')

# Adding students, subjects and marks
@login_required(login_url = 'login')
def add_student(request):
    if request.method == 'POST':
        student = request.POST['studentname']
        subject = request.POST['subject']
        marks = request.POST['marks']
        try:
            # Checking student exists in database
            student_model = StudentModel.objects.get(name = student, admin = request.user)
        except:
            # Adding new student and subject
            student_model = StudentModel.objects.create(name = student, admin = request.user)
            student_model.save()
            subject_model = SubjectsModel.objects.create(student = student_model, subject = subject, marks = marks)
            subject_model.save()
            return redirect('dashboard')
        else:
            # Checking subjects
            for subjects in student_model.subjectsmodel_set.all(): 
                # If subject exists upadating marks
                if subjects.subject == subject:
                    subject_model = SubjectsModel.objects.get(student = student_model, subject = subject)
                    subject_model.marks += int(marks)
                    subject_model.save()
                    return redirect('dashboard')  

            # If subject not exists creating new subjects
            subject_model = SubjectsModel.objects.create(student = student_model, subject = subject, marks = marks)
            subject_model.save()
            return redirect('dashboard')    

    else:
        return render(request, 'students/add_student.html')