# Generated by Django 3.0.3 on 2020-02-19 19:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wishapp', '0002_auto_20200219_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishmodel',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='wishmodel',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
