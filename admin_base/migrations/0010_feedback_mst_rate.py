# Generated by Django 3.1.4 on 2021-03-04 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_base', '0009_auto_20210305_0025'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback_mst',
            name='rate',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=5),
        ),
    ]