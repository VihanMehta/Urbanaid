# Generated by Django 3.1.4 on 2021-02-04 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usr_base', '0004_auto_20210204_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='Name',
            field=models.CharField(max_length=25),
        ),
    ]