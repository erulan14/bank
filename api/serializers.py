from rest_framework import serializers
from main.models import *
from django.contrib.auth.models import User


class CardsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cards
        fields = ("id", "name", "card_number", "card_code", "card_release", "card_ending", "balance", "creator")

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", 'username', 'first_name', 'last_name', 'email')


class AccountSerializers(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ("id", "user", "phone", "birth_date", "avatar", "location", "cards")


