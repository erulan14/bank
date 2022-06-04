from django.db import models
from django.contrib.auth.models import User


class Cards(models.Model):
    name = models.CharField(max_length=20, verbose_name="Имя карты")
    card_number = models.CharField(max_length=16, verbose_name="Номер карты")
    card_code = models.IntegerField(verbose_name="Код карты")
    card_release = models.DateField(verbose_name="Выпуск карты")
    card_ending = models.DateField(verbose_name="Срок карты")

    balance = models.DecimalField(default=0, max_digits=13, decimal_places=2, verbose_name="Баланс")
    creator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Создатель")

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = "Карта"
        verbose_name_plural = "Карты"



class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    phone = models.CharField(max_length=15, verbose_name="Номер телефона")
    birth_date = models.DateField(verbose_name="Дата рождения")
    avatar = models.ImageField(upload_to="account/avatar/", verbose_name="Фото профиля")
    location = models.CharField(max_length=40, verbose_name="Локация")
    cards = models.ManyToManyField(Cards, verbose_name="Карты")

    #balance = models.DecimalField(default=0, max_digits=13, decimal_places=2, verbose_name="Баланс")

    def __str__(self):
        return "{}".format(self.phone)

    class Meta:
        verbose_name = "Аккаунт"
        verbose_name_plural = "Аккаунты"
