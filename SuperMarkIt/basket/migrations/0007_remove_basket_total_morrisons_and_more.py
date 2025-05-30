# Generated by Django 5.2 on 2025-04-18 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0006_auto_20191115_1735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='total_morrisons',
        ),
        migrations.RemoveField(
            model_name='basket',
            name='total_sainsburys',
        ),
        migrations.RemoveField(
            model_name='basket',
            name='total_tesco',
        ),
        migrations.AddField(
            model_name='basket',
            name='total_amazon',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='basket',
            name='total_flipkart',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='basket',
            name='total_myntra',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
