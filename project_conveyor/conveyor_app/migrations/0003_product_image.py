# Generated by Django 4.0.4 on 2022-09-08 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conveyor_app', '0002_customer_order_product_shippingadress_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]