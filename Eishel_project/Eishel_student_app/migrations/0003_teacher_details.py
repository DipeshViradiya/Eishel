# Generated by Django 3.1.7 on 2021-03-20 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eishel_student_app', '0002_remove_student_details_st_dob'),
    ]

    operations = [
        migrations.CreateModel(
            name='teacher_details',
            fields=[
                ('tc_username', models.CharField(max_length=25)),
                ('tc_email', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('tc_pass', models.CharField(max_length=25)),
                ('tc_clgname', models.CharField(max_length=25)),
            ],
        ),
    ]