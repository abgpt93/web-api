# Generated by Django 3.2.4 on 2021-06-11 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_rename_created_at_tweet_posted_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='posted_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
