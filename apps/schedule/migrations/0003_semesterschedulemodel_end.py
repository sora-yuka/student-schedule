# Generated by Django 5.1.2 on 2025-01-27 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_alter_lessonmodel_week_variance_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='semesterschedulemodel',
            name='end',
            field=models.DateField(default='2025-01-20'),
            preserve_default=False,
        ),
    ]
