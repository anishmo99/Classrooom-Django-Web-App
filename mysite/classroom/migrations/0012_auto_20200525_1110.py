# Generated by Django 3.0.5 on 2020-05-25 05:40

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0011_auto_20200525_1040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='student_name',
        ),
        migrations.AddField(
            model_name='student',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='date joined'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(default='', max_length=60, unique=True, verbose_name='email'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='student',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='is_student',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='student',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='last_login',
            field=models.DateTimeField(auto_now=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(default='', max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='username',
            field=models.CharField(default='', max_length=30, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='answer',
            name='answer_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 25, 5, 40, 39, 867773, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 25, 5, 40, 39, 867219, tzinfo=utc), verbose_name='date published'),
        ),
    ]
