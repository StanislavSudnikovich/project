# Generated by Django 4.1.3 on 2022-12-16 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0020_comment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='Review',
        ),
    ]
