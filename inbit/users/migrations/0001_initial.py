# Generated by Django 3.0.6 on 2020-09-21 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('email', models.EmailField(max_length=50, primary_key=True, serialize=False, verbose_name='Email')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('password', models.CharField(max_length=100, verbose_name='password')),
                ('phone_num', models.IntegerField(max_length=20, verbose_name='phone number')),
                ('position', models.IntegerField(max_length=20, verbose_name='School positino')),
            ],
            options={
                'verbose_name': 'Users',
                'ordering': ['position'],
            },
        ),
    ]