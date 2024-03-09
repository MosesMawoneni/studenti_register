from django.contrib import admin

from . import models


admin.site.register(models.CourseAttendance)
admin.site.register(models.DailyRegister)
