# Generated by Django 5.1.2 on 2025-01-31 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofilemodel',
            name='pfp',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
    ]
