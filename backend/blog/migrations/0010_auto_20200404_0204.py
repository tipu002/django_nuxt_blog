# Generated by Django 3.0.5 on 2020-04-03 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200403_2326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posttag',
            name='post',
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='tags',
            field=models.ManyToManyField(blank=True, default=None, to='blog.PostTag'),
        ),
    ]