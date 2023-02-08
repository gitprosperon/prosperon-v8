# Generated by Django 4.1.4 on 2023-02-07 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0046_alter_student_graduation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='graduation_date',
            field=models.CharField(blank=True, choices=[('Spring 2023', 'Spring 2023'), ('Fall 2023', 'Fall 2023'), ('Spring 2024', 'Spring 2024'), ('Fall 2024', 'Fall 2024'), ('Spring 2025', 'Spring 2025'), ('Fall 2025', 'Fall 2025')], max_length=200, null=True),
        ),
    ]
