# Generated by Django 3.1.4 on 2021-03-03 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usr_base', '0001_initial'),
        ('admin_base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking_slot',
            name='user',
            field=models.ForeignKey(max_length=20, on_delete=django.db.models.deletion.CASCADE, to='usr_base.user_mst'),
        ),
        migrations.AlterField(
            model_name='service_mst',
            name='ServiceName',
            field=models.CharField(db_index=True, max_length=355),
        ),
        migrations.AlterField(
            model_name='service_mst',
            name='slug',
            field=models.SlugField(max_length=455, unique=True),
        ),
    ]
