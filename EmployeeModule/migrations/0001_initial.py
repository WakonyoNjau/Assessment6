# Generated by Django 5.0.2 on 2024-02-29 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('emp_code', models.CharField(max_length=50)),
                ('mobile_no', models.CharField(max_length=10)),
                ('position', models.CharField(max_length=10)),
            ],
        ),
    ]
