# Generated by Django 3.0.2 on 2020-01-23 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avr_rigney', '0002_auto_20200116_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lightmodule',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
