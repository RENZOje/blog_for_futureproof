# Generated by Django 3.1.1 on 2020-09-12 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200912_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='time_creation',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='time_last_update',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]