# Generated by Django 4.2.3 on 2023-08-09 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extra',
            name='per',
            field=models.CharField(choices=[('Per day', 'Per day'), ('Per person', 'Per person'), ('Per day / per person', 'Per day / per person'), ('Per booking', 'Per booking')], max_length=50),
        ),
    ]
