# Generated by Django 3.1.7 on 2021-03-31 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eishel_student_app', '0008_auto_20210329_1814'),
    ]

    operations = [
        migrations.CreateModel(
            name='temp_ans_data',
            fields=[
                ('stu_id', models.IntegerField(primary_key=True, serialize=False)),
                ('stu_ans', models.TextField()),
            ],
        ),
    ]
