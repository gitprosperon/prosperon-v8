# Generated by Django 4.1.4 on 2023-01-30 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0062_alter_student_life_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='universitymodule',
            name='next_life_event',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
