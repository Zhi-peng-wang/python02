from django.db import models

# Create your models here.
class School(models.Model):
    school_id = models.IntegerField()
    school_name = models.CharField(max_length=20)

    def __str__(self):
        return self.school_name

class Manager(models.Model):
    manager_id = models.IntegerField()
    manager_name = models.CharField(max_length=20)
    # 表示学校和管理者是一对一的
    my_school = models.OneToOneField(School)

    def __str__(self):
        return self.manager_name

class Teacher(models.Model):
    teacher_name = models.CharField(max_length=10)
    my_school = models.ForeignKey("School")

    def __str__(self):
        return self.teacher_name

class Student(models.Model):
    student_name = models.CharField(max_length=10)
    teachers = models.ManyToManyField("Teacher")

    def __str__(self):
        return self.student_name
