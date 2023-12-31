# Generated by Django 4.2.6 on 2023-11-01 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GreenhouseData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('moisture1', models.FloatField(null=True)),
                ('moisture2', models.FloatField(null=True)),
                ('temperature1', models.FloatField(null=True)),
                ('temperature2', models.FloatField(null=True)),
                ('humidity1', models.FloatField(null=True)),
                ('humidity2', models.FloatField(null=True)),
            ],
        ),
    ]
