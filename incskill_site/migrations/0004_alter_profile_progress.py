# Generated by Django 3.2.15 on 2022-11-03 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incskill_site', '0003_profile_quiz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='progress',
            field=models.IntegerField(default=0),
        ),
    ]