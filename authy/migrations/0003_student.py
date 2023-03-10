# Generated by Django 4.1.6 on 2023-02-15 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authy', '0002_user_is_active_user_is_staff_alter_user_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_number', models.CharField(max_length=10)),
                ('student_name', models.CharField(max_length=100)),
                ('faculty_name', models.CharField(max_length=100)),
                ('student_email', models.CharField(max_length=256)),
                ('date_of_birth', models.DateTimeField()),
            ],
        ),
    ]
