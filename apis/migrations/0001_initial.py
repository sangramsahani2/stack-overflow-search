# Generated by Django 4.1.1 on 2022-09-16 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='qustions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=30)),
                ('link', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=500)),
            ],
        ),
    ]
