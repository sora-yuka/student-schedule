# Generated by Django 5.1.2 on 2024-10-28 16:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('faculties', '0001_initial'),
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('today', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=100)),
                ('fifth_lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fifth_lesson_set', to='lessons.lessonsmodel')),
                ('first_lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='first_lesson_set', to='lessons.lessonsmodel')),
                ('fourth_lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fourth_lesson_set', to='lessons.lessonsmodel')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faculties.groupsmodel')),
                ('second_lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='second_lesson_set', to='lessons.lessonsmodel')),
                ('seventh_lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seventh_lesson_set', to='lessons.lessonsmodel')),
                ('sixth_lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sixth_lesson_set', to='lessons.lessonsmodel')),
                ('third_lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='third_lesson_set', to='lessons.lessonsmodel')),
            ],
        ),
    ]