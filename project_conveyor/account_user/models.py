from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# from project_conveyor.account_user.manager import ConveyorUserManager


# class ConveyorUser(AbstractBaseUser, PermissionsMixin):
#     USERNAME_LENGTH = 40
#     username = models.CharField(
#         max_length=USERNAME_LENGTH,
#         unique=True,
#     )
#
#     data_joined = models.DateTimeField(
#         auto_now_add=True,
#     )
#     is_staff = models.BooleanField(
#         default=False,
#     )
#
#     USERNAME_FIELD = 'username'
#
#     objects = ConveyorUserManager()



class Profile(models.Model):
    BLAGOEVGRAD = 'Благоевград'
    DOBRICH = 'Добрич'
    PLEVEN = 'Плевен'
    SOFIA = 'София'
    BURGAS = 'Бургас'
    KARDZHALI = 'Кърджали'
    PLOVDIV = 'Пловдив'
    VARNA = 'Варна'
    KUSTENDIL = 'Кюстендил'
    RAZGRAD = 'Разград'
    STARA_ZAGORA = 'Стара Загора'
    VELIKO_TURNOVO = 'Велико Търново'
    LOVECH = 'Ловеч'
    RUSE = 'Русе'
    TURGOVISHTE = 'Търговище'
    VIDIN = 'Видин'
    MONTANA = 'Монтана'
    SILISTRA = 'Силистра'
    HASKOVO = 'Хасково'
    VRATSA = 'Враца'
    PAZARDZHIK = 'Пазарджик'
    SLIVEN = 'Сливен'
    SHUMEN = 'Шумен'
    GABROVO = 'Габрово'
    PERNIK = 'Перник'
    SMOLYAN = 'Смолян'
    YAMBOL = 'Ямбол'

    REGION_CHOICE = [(x, x) for x in (BLAGOEVGRAD, DOBRICH, PLEVEN, SOFIA, BURGAS, KARDZHALI, PLOVDIV,
                                      VARNA, KUSTENDIL, RAZGRAD, STARA_ZAGORA, VELIKO_TURNOVO, LOVECH,
                                      RUSE, TURGOVISHTE, VIDIN, MONTANA, SILISTRA, HASKOVO, VRATSA,
                                      PAZARDZHIK, SLIVEN, SHUMEN, GABROVO, PERNIK, SMOLYAN, YAMBOL,)]

    MAX_LENGTH_FIRST_NAME = 30
    MAX_LENGTH_LAST_NAME = 30
    MAX_LENGTH_COUNTRY_NAME = 40
    MAX_LENGTH_CITY_NAME = 40

    first_name = models.CharField(
        max_length=MAX_LENGTH_FIRST_NAME,
        verbose_name='Име',
    )

    last_name = models.CharField(
        max_length=MAX_LENGTH_LAST_NAME,
        verbose_name='Фамилия',
    )

    email = models.EmailField(
        verbose_name='Ел.Поща'
    )

    phone_number = models.IntegerField(
        verbose_name='Телефонен номер'
    )

    username = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    addres = models.TextField(
        verbose_name='Адрес'
    )

    country = models.CharField(
        max_length=MAX_LENGTH_COUNTRY_NAME,
    )

    region = models.CharField(
        max_length=max(len(x) for (x, _) in REGION_CHOICE)
    )
