# Generated by Django 4.0.4 on 2022-08-24 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conveyor_app', '0003_userpurchases_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpurchases',
            name='quantity',
        ),
        migrations.AddField(
            model_name='ucflbodies',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
