# Generated by Django 4.1.4 on 2023-01-30 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0059_alter_student_course_progress'),
    ]

    operations = [
        migrations.AddField(
            model_name='anytimedecision',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='anytimeImages/'),
        ),
    ]
