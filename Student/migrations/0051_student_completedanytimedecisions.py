# Generated by Django 4.1.4 on 2023-02-07 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0050_student_net_income_monthly_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='completedAnytimeDecisions',
            field=models.CharField(blank=True, max_length=100000, null=True),
        ),
    ]
