# Generated by Django 2.1.5 on 2019-01-23 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='rate',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
