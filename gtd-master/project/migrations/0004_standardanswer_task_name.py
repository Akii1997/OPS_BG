# Generated by Django 2.2.2 on 2019-06-23 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_remove_standardanswer_task_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='standardanswer',
            name='task_name',
            field=models.CharField(default='Task Heading', max_length=500),
        ),
    ]
