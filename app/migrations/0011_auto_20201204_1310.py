# Generated by Django 3.1.3 on 2020-12-04 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20201204_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='trade',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
    ]
