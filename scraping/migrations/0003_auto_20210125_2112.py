# Generated by Django 3.0.5 on 2021-01-25 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0002_auto_20210125_2028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='image',
        ),
        migrations.AddField(
            model_name='news',
            name='image_url',
            field=models.URLField(max_length=500, null=True),
        ),
    ]
