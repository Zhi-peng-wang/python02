from django.db import models
import time
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()

class ClassRoom(models.Model):
    roomID = models.IntegerField()
    loc = models.CharField(max_length=10)
    roomName = models.CharField(max_length=20)

    def __str__(self):
        return self.roomName

class Teacher(models.Model):
    name = models.CharField(max_length=10)
    course = models.CharField(max_length=10)

    room = models.OneToOneField(ClassRoom)

    def getRoomName(self):
        return self.room.roomName

    getRoomName.short_description = "教室 "

    def curTime(self):
        return time.time()

    curTime.short_description = "当前时间"
    # 根据name排序
    curTime.admin_order_field = "name"
    def __str__(self):
        return self.name

class Students(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()

    room = models.ForeignKey(ClassRoom)
    def __str__(self):
        return self.name