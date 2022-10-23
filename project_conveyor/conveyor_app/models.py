from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from jsonfield import JSONField


# Create your models here.
# -*- coding: utf-8 -*-



class AskModel(models.Model):
    MAX_LENGTH_NAME = 50

    TEXTILE_TAPE_WITHOUT_COVERAGE = 'Текстилна лента без покритие'
    TEXTILE_TAPE_WITH_PVC_COVERAGE = 'Текстилна лента с PVC покритие'
    TEXTILE_TAPE_WITH_PU_COVERAGE = 'Текстилна лента с PU покритие'
    TEXTILE_TAPE_WITH_TPO_COVERAGE = 'Текстилна лента с TPO покритие'
    TEXTILE_TAPE_WITH_RUBBER_COVERAGE = 'Текстилна лента с гумено покритие'

    TYPE_TEXTILE = [(x, x) for x in (
    TEXTILE_TAPE_WITHOUT_COVERAGE, TEXTILE_TAPE_WITH_PVC_COVERAGE, TEXTILE_TAPE_WITH_PU_COVERAGE,
    TEXTILE_TAPE_WITH_TPO_COVERAGE, TEXTILE_TAPE_WITH_RUBBER_COVERAGE)]

    CONNECTION_METHOD_OPEN = 'Отворена'
    CONNECTION_METHOD_GLUED = 'Залепена'
    CONNECTION_METHOD_METAL = 'Метална връзка'

    TYPE_CONNECTION = [(x, x) for x in (CONNECTION_METHOD_OPEN, CONNECTION_METHOD_GLUED, CONNECTION_METHOD_METAL)]

    name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        verbose_name='Име',
    )
    telephone = models.IntegerField(
        verbose_name='Телефон',
        null=True,
        blank=True,
    )

    type_of_tape = models.CharField(
        max_length=max(len(x) for (x, _) in TYPE_TEXTILE),
        choices=TYPE_TEXTILE,
        verbose_name='Вид лента',

    )

    connection_method = models.CharField(
        max_length=max(len(x) for (x, _) in TYPE_CONNECTION),
        choices=TYPE_CONNECTION,
        verbose_name='Начин на свързване',
    )

    width = models.FloatField(
        verbose_name='Ширина',
        null=True,
        blank=True,
    )

    length = models.FloatField(
        verbose_name='Дължина',
        null=True,
        blank=True,
    )

    blade_height = models.FloatField(
        verbose_name='Височина на лопатките',
        null=True,
        blank=True,
    )

    blade_length = models.FloatField(
        verbose_name='Дължина на лопатките',
        null=True,
        blank=True,
    )

    step_between_blades = models.FloatField(
        verbose_name='Стъпка между лопатките',
        null=True,
        blank=True,
    )

    height_of_side_stops = models.FloatField(
        verbose_name='Височина на странични ограничители',
        null=True,
        blank=True,

    )

    description = models.TextField(
        verbose_name='Относно',
        null=True,
        blank=True,
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )


class Customer(models.Model):
    user = models.OneToOneField(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    name = models.CharField(
        max_length=200,
        null=True,
    )

    email = models.CharField(
        max_length=200,
        null=True,
    )

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(
        max_length=200,
        null=True,
    )

    price = models.FloatField()

    digital = models.BooleanField(default=False, null=True, blank=True)

    image = models.ImageField(
        null=True,
        blank=True,
    )

    diameter = models.FloatField(
        null=True,
        blank=True,
    )

    D_3 = models.FloatField(
        null=True,
        blank=True,
        verbose_name='D3'
    )

    E = models.FloatField(
        null=True,
        blank=True,
    )

    B = models.FloatField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Order(models.Model):
    customer = models.ForeignKey(
        'Customer',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    date_ordered = models.DateTimeField(
        auto_now_add=True
    )

    complete = models.BooleanField(
        default=False,
        null=True,
        blank=True,
    )

    transaction_id = models.CharField(
        max_length=200,
        null=True,
    )

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(
        'Product',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    order = models.ForeignKey(
        'Order',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    quantity = models.IntegerField(
        default=0,
        null=True,
        blank=True,
    )

    date_added = models.DateTimeField(
        auto_now_add=True,
    )

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

class ShippingAdress(models.Model):
    customer = models.ForeignKey(
        'Customer',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    order = models.ForeignKey(
        'Order',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    address = models.CharField(
        max_length=200,
        null=True,
        verbose_name='Адрес'
    )

    city = models.CharField(
        max_length=200,
        null=True,
        verbose_name='Град'
    )

    state = models.CharField(
        max_length=200,
        null=True,
        verbose_name='Област'
    )

    zipcode = models.CharField(
        max_length=200,
        null=True,
        verbose_name='Пощенски код'
    )

    date_added = models.CharField(
        max_length=200,
        null=True,
    )

    email = models.EmailField(
        null=True,
    )

    def __str__(self):
        return self.address


