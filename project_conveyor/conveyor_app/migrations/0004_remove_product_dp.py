# Generated by Django 4.0.4 on 2022-11-06 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conveyor_app', '0003_product_de_product_dg_product_dp_product_sj_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='dp',
        ),
    ]
