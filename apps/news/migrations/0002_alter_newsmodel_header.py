# Generated by Django 5.1.2 on 2025-03-08 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsmodel',
            name='header',
            field=models.CharField(max_length=200),
        ),
    ]
