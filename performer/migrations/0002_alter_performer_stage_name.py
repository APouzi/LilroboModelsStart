# Generated by Django 3.2.4 on 2021-06-27 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performer',
            name='stage_name',
            field=models.CharField(max_length=200),
        ),
    ]
