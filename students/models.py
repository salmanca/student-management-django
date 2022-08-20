from django.db import models
from django.contrib.auth.models import User

class StudentModel(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self):
        return self.name

class SubjectsModel(models.Model):
    student = models.ForeignKey(StudentModel, on_delete=models.CASCADE)
    subject = models.CharField(max_length=150, null=False, blank=False)
    marks = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.student.name