# Generated by Django 4.1.4 on 2023-03-14 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0084_alter_student_birth_day_alter_student_birth_month_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='completedAnytimeDecisions',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]