# Generated by Django 3.0.5 on 2021-01-20 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usr_base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_mst',
            name='Password',
            field=models.CharField(max_length=500),
        ),
    ]
