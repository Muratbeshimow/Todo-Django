# Generated by Django 4.2.7 on 2024-01-26 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0008_alter_task_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.CharField(max_length=20),
        ),
    ]
