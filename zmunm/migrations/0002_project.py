# Generated by Django 2.1.2 on 2018-10-28 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zmunm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_date', models.DateTimeField(auto_created=True, auto_now=True)),
                ('company', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('memo', models.CharField(max_length=200)),
            ],
        ),
    ]
