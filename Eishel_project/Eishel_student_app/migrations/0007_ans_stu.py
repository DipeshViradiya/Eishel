# Generated by Django 3.1.7 on 2021-03-29 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eishel_student_app', '0006_auto_20210327_1037'),
    ]

    operations = [
        migrations.CreateModel(
            name='ans_stu',
            fields=[
                ('exam_id', models.CharField(default='exam_dbms', max_length=25, primary_key=True, serialize=False)),
                ('ex_q_no', models.IntegerField(default=1)),
                ('ans_by_stu', models.TextField()),
            ],
        ),
    ]
