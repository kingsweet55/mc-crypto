# Generated by Django 2.0.1 on 2018-03-01 14:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20180301_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='support_staff',
            field=models.CharField(default=uuid.uuid4, max_length=100, unique=True),
        ),
    ]
