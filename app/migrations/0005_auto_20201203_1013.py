# Generated by Django 3.1.3 on 2020-12-03 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20201203_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='items',
            field=models.ManyToManyField(to='app.Item'),
        ),
    ]
