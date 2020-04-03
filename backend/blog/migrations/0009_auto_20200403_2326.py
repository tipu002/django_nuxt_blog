# Generated by Django 3.0.5 on 2020-04-03 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200403_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='sub_category',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_sub_category', to='blog.PostSubCategory'),
        ),
    ]