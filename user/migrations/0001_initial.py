# Generated by Django 4.2.1 on 2023-05-26 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('surname', models.CharField(max_length=16)),
                ('gender', models.IntegerField(choices=[(1, 'Women'), (2, 'Men')])),
            ],
        ),
    ]
