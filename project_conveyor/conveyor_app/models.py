from django.contrib.auth import get_user_model
from django.db import models
from jsonfield import JSONField

# Create your models here.
# -*- coding: utf-8 -*-

UserModel = get_user_model()


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
        UserModel,
        on_delete=models.CASCADE,
    )


class UCFnumber(models.Model):
    UCF_101 = 'UCF 101'
    UCF_102 = 'UCF 102'
    UCF_103 = 'UCF 103'
    UCF_104 = 'UCF 104'
    UCF_105 = 'UCF 105'
    UCF_106 = 'UCF 106'
    UCF_107 = 'UCF 107'
    UCF_108 = 'UCF 108'
    UCF_109 = 'UCF 109'
    UCF_110 = 'UCF 110'
    UCF_111 = 'UCF 111'

    UCF_CHOICES = [(x, x) for x in
                   (UCF_101, UCF_102, UCF_103, UCF_104, UCF_105, UCF_106, UCF_107, UCF_108, UCF_109, UCF_110, UCF_111)]

    ucf_number = models.CharField(
        max_length=max(len(x) for (x, _) in UCF_CHOICES),
        choices=UCF_CHOICES,
        verbose_name='UCF No.'
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

class UCFLbodies(models.Model):

    name = models.CharField(
        max_length=30,
    )

    UCFL_N = models.IntegerField()

    D_3 = models.FloatField()

    E = models.FloatField()

    B = models.FloatField()

    F = models.FloatField()

    L = models.FloatField()

    H = models.FloatField()

    price = models.FloatField(
        verbose_name='Цена'
    )


    # user = models.ForeignKey(
    #     UserModel,
    #     on_delete=models.CASCADE,
    # )

    def __str__(self):
        return f'{self.name} {self.UCFL_N}'

class UserPurchases(models.Model):
    UCF_ids = models.ForeignKey(
        'UCFLbodies',
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    quantity = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Количество',
    )
