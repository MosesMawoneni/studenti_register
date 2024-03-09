from django.db import models
from accounts.models import Student, Tutor


class DailyRegister(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    time_start = models.TimeField()
    time_end = models.TimeField()
    is_present = models.BooleanField(default=True)
    register_tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.student)


class CourseAttendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    name_of_course = models.CharField(max_length=255)
    start_time = models.TimeField()
    end_time = models.TimeField()
    course_tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    is_attending = models.BooleanField(default=False)

    def __str__(self):
        return self.name_of_course
