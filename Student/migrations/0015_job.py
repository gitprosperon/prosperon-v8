# Generated by Django 4.1.4 on 2022-12-29 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0014_video_progress'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=400, null=True)),
                ('company', models.CharField(blank=True, max_length=400, null=True)),
                ('location', models.CharField(blank=True, max_length=400, null=True)),
            ],
        ),
    ]
