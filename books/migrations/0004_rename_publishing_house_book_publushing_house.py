# Generated by Django 3.2.5 on 2021-07-22 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20210722_1908'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='publishing_house',
            new_name='publushing_house',
        ),
    ]
