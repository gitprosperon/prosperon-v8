# Generated by Django 4.1.4 on 2023-02-07 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0049_student_current_month'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='net_income_monthly_list',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
