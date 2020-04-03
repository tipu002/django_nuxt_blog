# Generated by Django 3.0.5 on 2020-04-03 17:22

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200403_0113'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='post_image',
            field=imagekit.models.fields.ProcessedImageField(default=None, null=True, upload_to='post-images'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='post_thumbnail',
            field=imagekit.models.fields.ProcessedImageField(default=None, null=True, upload_to='post-images/thumbnails'),
        ),
    ]