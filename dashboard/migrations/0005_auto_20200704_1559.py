# Generated by Django 3.0.7 on 2020-07-04 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20200704_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='senior_users',
            name='name',
            field=models.CharField(default='Cool Senior', max_length=264),
        ),
        migrations.AlterField(
            model_name='senior_users',
            name='nick_name',
            field=models.CharField(default='stud', max_length=264),
        ),
        migrations.AlterField(
            model_name='senior_users',
            name='story_name',
            field=models.CharField(default='phuk', max_length=264),
        ),
        migrations.AlterField(
            model_name='senior_users',
            name='tag_line',
            field=models.CharField(default='I am Cool...', max_length=264),
        ),
    ]
