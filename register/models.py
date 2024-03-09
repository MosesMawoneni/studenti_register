from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Student(models.Model):
    MALE_CHOICE = "MALE"
    FEMALE_CHOICE = "FEMALE"
    GENDER_CHOICES = [(MALE_CHOICE, "Male"), (FEMALE_CHOICE, "Female")]

    student = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    location = models.CharField(max_length=255)
    bio = models.TextField()
    date_of_birth = models.DateField()
    date_enrolled = models.DateField()
    name_of_guardian = models.CharField(max_length=255)
    is_prefect = models.BooleanField(default=False)
    gender = models.CharField(choices=GENDER_CHOICES)

    def __str__(self):
        return str(self.student)


class Tutor(models.Model):
    MALE_CHOICE = "MALE"
    FEMALE_CHOICE = "FEMALE"
    GENDER_CHOICES = [(MALE_CHOICE, "Male"), (FEMALE_CHOICE, "Female")]

    SINGLE_CHOICE = "SINGLE"
    MARRIED_CHOICE = "MARRIED"
    MARITAL_STATUS_CHOICES = [(SINGLE_CHOICE, "Single"), (MARRIED_CHOICE, "Married")]

    tutor = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    location = models.CharField(max_length=255)
    bio = models.TextField()
    date_of_birth = models.DateField()
    date_engaged = models.DateField()
    name_of_spouse = models.CharField(max_length=255, blank=True, null=True)
    marital_status = models.CharField(max_length=255, choices=MARITAL_STATUS_CHOICES)
    gender = models.CharField(choices=GENDER_CHOICES)

    def __str__(self):
        return str(self.tutor)


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
