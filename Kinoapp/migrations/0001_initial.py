# Generated by Django 4.0.5 on 2022-06-25 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aktyor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=30)),
                ('mamlakat', models.CharField(max_length=60)),
                ('erkakmi', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Kino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('yil', models.DateField()),
                ('janr', models.CharField(max_length=50)),
                ('aktyorlar', models.ManyToManyField(to='Kinoapp.aktyor')),
            ],
        ),
    ]
