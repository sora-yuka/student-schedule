# Generated by Django 5.1.2 on 2024-10-28 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LessonsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_type', models.CharField(choices=[('Practice', 'Practice'), ('Lecture', 'Lecture')], max_length=100)),
                ('class_room', models.CharField(max_length=200)),
                ('lesson_name', models.CharField(max_length=200)),
                ('professor', models.CharField(max_length=200)),
                ('number_of_weeks', models.CharField(max_length=50)),
            ],
        ),
    ]
