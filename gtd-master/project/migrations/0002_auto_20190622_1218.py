# Generated by Django 2.2.2 on 2019-06-22 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formquestions',
            name='assigned_by',
            field=models.CharField(default='abc', max_length=50),
        ),
        migrations.AlterField(
            model_name='formquestions',
            name='gm_name',
            field=models.CharField(default='abc', max_length=50, verbose_name='GM Name'),
        ),
    ]
