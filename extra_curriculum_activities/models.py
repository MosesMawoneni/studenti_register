from django.db import models

from accounts.models import Tutor, Student


class ExtraActivities(models.Model):
    class Activities(models.TextChoices):
        SOCCER = "soccer"
        NETBALL = "netball"
        TRADITIONAL_DANCE = "traditional dance"
        TENNIS = "tennis"
        ATHLETICS = "athletics"
        SWIMMING = "swimming"
        HOCKEY = "hockey"
        RUGBY = "rugby"
        BASEBALL = "baseball"
        BOXING = "boxing"
        HANDBALL = "handball"
        WRESTLING = "wrestling"
        PUBLIC_SPEAKING = "public speaking"
        SCRIPTURE_UNION = "scripture union"
        BASKETBALL = "basketball"
        JAVELIN = "javelin"
        SHORT_PUT = "short put"
        DISCUS = "discus"
        NONE = "Not involved in any extra_curriculum activity"

    class DaysEngaged(models.TextChoices):
        MONDAY = "monday"
        TUESDAY = "tuesday"
        WEDNESDAY = "wednesday"
        THURSDAY = "thursday"
        FRIDAY = "friday"
        SATURDAY = "saturday"
        SUNDAY = "sunday"

    sport = models.CharField(max_length=255, choices=Activities)
    tutor_trainer = models.ManyToManyField(Tutor)
    student = models.ManyToManyField(Student)
    start_time = models.TimeField()
    end_time = models.TimeField()
    day = models.CharField(max_length=255, choices=DaysEngaged)

    def __str__(self):
        return self.sport
