# Generated by Django 3.0.3 on 2020-02-20 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishapp', '0008_auto_20200220_1141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishmodel',
            name='uuid',
        ),
        migrations.AddField(
            model_name='wishmodel',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
