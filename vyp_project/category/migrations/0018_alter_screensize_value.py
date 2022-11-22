# Generated by Django 4.1.3 on 2022-11-21 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0017_alter_screensize_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screensize',
            name='value',
            field=models.DecimalField(decimal_places=1, help_text='Дюймы', max_digits=2),
        ),
    ]
