# Generated by Django 3.2.9 on 2021-11-21 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpleDataApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatasetName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]
