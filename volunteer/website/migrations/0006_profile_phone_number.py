# Generated by Django 3.2.7 on 2021-09-19 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_alter_profile_managers'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(default='0123456789', max_length=10),
        ),
    ]