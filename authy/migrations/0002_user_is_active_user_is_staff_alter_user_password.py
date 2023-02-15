# Generated by Django 4.1.6 on 2023-02-15 07:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False, help_text='Is the user account active? Default is False.'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Is the user a staff? Default is False.'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=128, validators=[django.core.validators.MaxLengthValidator(limit_value=128)]),
            preserve_default=False,
        ),
    ]