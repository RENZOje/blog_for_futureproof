# Generated by Django 3.1.1 on 2020-09-12 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200912_1724'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='publish',
        ),
        migrations.AddField(
            model_name='post',
            name='time_publish',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
