# Generated by Django 4.1.4 on 2023-02-08 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0052_rename_net_income_monthly_list_student_net_worth_monthly_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='current_year',
            field=models.CharField(blank=True, max_length=100000, null=True),
        ),
    ]
