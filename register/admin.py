from django.contrib import admin

from . import models

admin.site.register(models.Student)
admin.site.register(models.Tutor)
admin.site.register(models.CourseAttendance)
admin.site.register(models.DailyRegister)
