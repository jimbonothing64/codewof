# Generated by Django 2.1.5 on 2019-08-11 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Student'), (2, 'Teacher')], default=1),
        ),
    ]