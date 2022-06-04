from django.contrib import admin
from .models import Account, Cards


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("user", "phone", "birth_date", "location")


@admin.register(Cards)
class CardsAdmin(admin.ModelAdmin):
    list_display = ("name", "card_number", "card_code", "card_release", "card_ending", "balance")