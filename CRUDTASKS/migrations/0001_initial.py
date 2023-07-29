# Generated by Django 4.0.6 on 2023-07-26 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TasksInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=500)),
                ('due_date', models.DateField()),
                ('priority_levels', models.CharField(max_length=10)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
    ]
