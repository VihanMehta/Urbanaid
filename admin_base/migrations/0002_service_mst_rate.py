# Generated by Django 3.1.4 on 2021-02-03 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service_mst',
            name='rate',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=5),
        ),
    ]
