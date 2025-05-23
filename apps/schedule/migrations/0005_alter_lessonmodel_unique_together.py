# Generated by Django 5.1.2 on 2025-05-24 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0004_alter_professormodel_owner'),
        ('schedule', '0004_alter_lessonmodel_professor'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='lessonmodel',
            unique_together={('professor', 'start_period', 'end_period')},
        ),
    ]
