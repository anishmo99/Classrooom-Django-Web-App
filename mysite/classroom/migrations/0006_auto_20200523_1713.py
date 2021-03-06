# Generated by Django 3.0.5 on 2020-05-23 17:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0005_auto_20200523_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 23, 17, 13, 37, 401734, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 23, 17, 13, 37, 401172, tzinfo=utc), verbose_name='date published'),
        ),
    ]
