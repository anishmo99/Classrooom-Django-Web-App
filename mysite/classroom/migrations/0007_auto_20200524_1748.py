# Generated by Django 3.0.5 on 2020-05-24 17:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0006_auto_20200523_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 24, 17, 48, 32, 616388, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 24, 17, 48, 32, 615571, tzinfo=utc), verbose_name='date published'),
        ),
    ]