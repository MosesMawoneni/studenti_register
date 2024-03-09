from django.db import models

from accounts.models import Tutor


class Level(models.Model):
    class FormLevel(models.IntegerChoices):
        FORM_ONE = 1
        FORM_TWO = 2
        FORM_THREE = 3
        FORM_FOUR = 4
        FORM_FIVE = 5
        FORM_SIX = 6

    form_level = models.IntegerField(choices=FormLevel, default=FormLevel.FORM_ONE)

    def __str__(self):
        return self.form_level


class Course(models.Model):
    class CourseName(models.TextChoices):
        BIOLOGY = "Biology"
        PHYSICS = "Physics"
        HERITAGE = "Heritage Studies"
        ENGLISH = "English"
        FRENCH = "French"
        CHINESE = "Chinese"
        MATHEMATICS = "Mathematics"
        SHONA = "Shona"
        NDEBELE = "Ndebele"
        COMBINED_SCIENCE = "Combined Science"
        COMPUTER_SCIENCE = "Computer Science"

    course_name = models.CharField(choices=CourseName)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    form_level = models.ManyToManyField(Level)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.course_name + " | " + self.form_level
