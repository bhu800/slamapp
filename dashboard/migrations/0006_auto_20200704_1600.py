# Generated by Django 3.0.7 on 2020-07-04 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20200704_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='senior_users',
            name='email',
            field=models.CharField(default='b16000@students.iitmani.ac.in', max_length=200),
        ),
    ]
