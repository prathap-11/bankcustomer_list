# Generated by Django 5.1.1 on 2024-09-09 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bank_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('place', models.TextField(default='chennai')),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.DateTimeField()),
            ],
        ),
    ]
