# Generated by Django 4.1.3 on 2022-11-17 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('add_date', models.DateTimeField(auto_now=True)),
                ('image', models.FileField(upload_to='img_category/')),
                ('text', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='news.text')),
            ],
        ),
    ]