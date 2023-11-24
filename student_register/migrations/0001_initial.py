# Generated by Django 4.2.7 on 2023-11-24 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
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
                ("fullname", models.CharField(max_length=100)),
                ("student_number", models.CharField(max_length=3)),
                ("student_class", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=100)),
                ("phonenumber", models.CharField(max_length=100)),
            ],
        ),
    ]
