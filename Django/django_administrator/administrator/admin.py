from django.contrib import admin

from administrator.models import Students, ClassRoom, Teacher
# Register your models here.

admin.site.site_header = "这是站头"
admin.site.site_title = "这是站标题"
admin.site.index_title = "这是首页标语"


class ClassRoomAdmin(admin.ModelAdmin):
    pass

class StudentsAdmin(admin.ModelAdmin):
    pass

class TeacherAdmin(admin.ModelAdmin):
    list_per_page = 2
    actions_on_bottom = True
    actions_on_top = False
    # 将显示的写入列表中
    list_display = ["name", "room", "curTime", "getRoomName"]
    search_fields = ["name"]

    # fields = ["name", "course"]

    fieldsets = (
        ("基本信息", {"fields": ["name"]}),
        ("其它信息", {"fields": ["room", "course"]}),
    )


admin.site.register(Students, StudentsAdmin)
admin.site.register(ClassRoom, ClassRoomAdmin)
admin.site.register(Teacher, TeacherAdmin)