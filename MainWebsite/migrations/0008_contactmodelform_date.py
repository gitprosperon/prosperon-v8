# Generated by Django 4.1.4 on 2023-02-17 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainWebsite', '0007_rename_contactform_contactmodelform'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmodelform',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
