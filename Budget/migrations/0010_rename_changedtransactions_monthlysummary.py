# Generated by Django 4.1.4 on 2023-01-17 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Budget', '0009_budgetitems_users_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ChangedTransactions',
            new_name='MonthlySummary',
        ),
    ]