# Generated by Django 3.1.7 on 2021-04-02 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eishel_student_app', '0011_model_features'),
    ]

    operations = [
        migrations.CreateModel(
            name='secondary_key_data',
            fields=[
                ('ex_id', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('secondary_key', models.TextField()),
            ],
        ),
    ]
