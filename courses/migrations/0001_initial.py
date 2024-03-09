# Generated by Django 5.0.3 on 2024-03-09 11:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("accounts", "0002_student_tutor"),
    ]

    operations = [
        migrations.CreateModel(
            name="Level",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "form_level",
                    models.IntegerField(
                        choices=[
                            (1, "Form One"),
                            (2, "Form Two"),
                            (3, "Form Three"),
                            (4, "Form Four"),
                            (5, "Form Five"),
                            (6, "Form Six"),
                        ],
                        default=1,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "course_name",
                    models.CharField(
                        choices=[
                            ("Biology", "Biology"),
                            ("Physics", "Physics"),
                            ("Heritage Studies", "Heritage"),
                            ("English", "English"),
                            ("French", "French"),
                            ("Chinese", "Chinese"),
                            ("Mathematics", "Mathematics"),
                            ("Shona", "Shona"),
                            ("Ndebele", "Ndebele"),
                            ("Combined Science", "Combined Science"),
                            ("Computer Science", "Computer Science"),
                        ]
                    ),
                ),
                ("start_time", models.TimeField()),
                ("end_time", models.TimeField()),
                (
                    "tutor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="accounts.tutor"
                    ),
                ),
                ("form_level", models.ManyToManyField(to="courses.level")),
            ],
        ),
    ]
