# Generated by Django 3.1.7 on 2021-03-20 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Eishel_student_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_details',
            name='st_dob',
        ),
    ]