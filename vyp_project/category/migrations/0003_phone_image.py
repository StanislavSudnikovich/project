# Generated by Django 4.1.3 on 2022-11-14 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_phone_add_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='image',
            field=models.ImageField(default=1, upload_to='img_category/'),
            preserve_default=False,
        ),
    ]
