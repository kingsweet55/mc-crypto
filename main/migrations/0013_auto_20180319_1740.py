# Generated by Django 2.0.1 on 2018-03-19 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20180318_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
