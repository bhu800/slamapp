# Generated by Django 3.0.7 on 2020-07-04 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20200704_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='senior_users',
            name='avatar',
            field=models.ImageField(default='static/dashboard/img/Avatars/background_removed.png', upload_to='static/dashboard/img/Avatars'),
        ),
    ]
