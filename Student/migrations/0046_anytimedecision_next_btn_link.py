# Generated by Django 4.1.4 on 2023-01-23 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0045_anytimedecision_learning_objectives_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='anytimedecision',
            name='next_btn_link',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
