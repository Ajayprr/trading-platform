# Generated by Django 3.1.3 on 2020-12-04 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20201203_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='item',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.item'),
        ),
    ]