# Generated by Django 2.0.1 on 2018-02-12 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cdc',
            name='COMP_CODES',
        ),
        migrations.RemoveField(
            model_name='courseslot',
            name='id',
        ),
        migrations.AddField(
            model_name='cdc',
            name='comp_codes',
            field=models.CharField(blank=True, max_length=5, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='courseslot',
            name='class_nbr',
            field=models.CharField(blank=True, max_length=4, primary_key=True, serialize=False),
        ),
    ]
