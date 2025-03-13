# Generated by Django 5.1.7 on 2025-03-11 21:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='assigned_to',
            field=models.ManyToManyField(related_name='tasks', to='tasks.employee'),
        ),
        migrations.AlterField(
            model_name='taskdetail',
            name='task',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='tasks.task'),
        ),
    ]
