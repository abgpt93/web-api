# Generated by Django 3.2.4 on 2021-06-12 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0004_auto_20210612_1905'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='user',
            new_name='name',
        ),
    ]
