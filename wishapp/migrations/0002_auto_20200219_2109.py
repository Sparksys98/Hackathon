# Generated by Django 3.0.3 on 2020-02-19 19:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wishapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishmodel',
            name='age',
        ),
        migrations.AddField(
            model_name='wishmodel',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='wishmodel',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
        migrations.AddField(
            model_name='wishmodel',
            name='person',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]