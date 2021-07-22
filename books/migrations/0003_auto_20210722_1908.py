# Generated by Django 3.2.5 on 2021-07-22 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20210720_1719'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='publshing_house',
            new_name='publishing_house',
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(related_name='author', to='books.Author'),
        ),
    ]