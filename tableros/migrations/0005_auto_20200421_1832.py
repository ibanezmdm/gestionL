# Generated by Django 2.1.15 on 2020-04-21 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tableros', '0004_auto_20200421_1831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tablero',
            name='url',
        ),
        migrations.AlterField(
            model_name='tablero',
            name='script',
            field=models.CharField(max_length=1000),
        ),
    ]