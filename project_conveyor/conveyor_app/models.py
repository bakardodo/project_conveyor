from django.contrib.auth import get_user_model
from django.db import models

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

    TYPE_TEXTILE = [(x, x)for x in (TEXTILE_TAPE_WITHOUT_COVERAGE, TEXTILE_TAPE_WITH_PVC_COVERAGE, TEXTILE_TAPE_WITH_PU_COVERAGE, TEXTILE_TAPE_WITH_TPO_COVERAGE, TEXTILE_TAPE_WITH_RUBBER_COVERAGE)]

    CONNECTION_METHOD_OPEN = 'Отворена'
    CONNECTION_METHOD_GLUED = 'Залепена'
    CONNECTION_METHOD_METAL = 'Метална връзка'

    TYPE_CONNECTION = [(x, x)for x in (CONNECTION_METHOD_OPEN, CONNECTION_METHOD_GLUED, CONNECTION_METHOD_METAL)]


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

class BearingBody(models.Model):
    UCF = 'UCF'
    UCFL = 'UCFL'
    UCP = 'UCP'
    UCT = 'UCT'

    TYPE_BEARING_BODY = [(x, x) for x in (UCF, UCFL, UCP, UCT)]

    bearing_body = models.CharField(
        max_length=max(len(x) for (x, _) in TYPE_BEARING_BODY),
        choices=TYPE_BEARING_BODY,
        verbose_name='Лагерно тяло',

    )


