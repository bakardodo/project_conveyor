# Generated by Django 4.0.4 on 2022-11-06 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conveyor_app', '0002_product_o_d_product_w'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='de',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='dg',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='dp',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='sj',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='sm',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
