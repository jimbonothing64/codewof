# Generated by Django 2.0.4 on 2018-08-03 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0018_auto_20180803_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='solution',
            field=models.TextField(blank=True),
        ),
    ]
