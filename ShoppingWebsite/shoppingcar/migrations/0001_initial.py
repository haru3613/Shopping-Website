# Generated by Django 2.0.1 on 2018-01-23 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppningCar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=128)),
                ('item', models.CharField(max_length=128)),
                ('count', models.IntegerField()),
            ],
        ),
    ]
