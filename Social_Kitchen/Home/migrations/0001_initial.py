# Generated by Django 3.2.6 on 2021-10-02 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TableReservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phoneNumber', models.CharField(max_length=10)),
                ('partySize', models.IntegerField(max_length=2)),
                ('time', models.TimeField()),
                ('date', models.DateField()),
            ],
        ),
    ]
