# Generated by Django 4.0.4 on 2022-06-04 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_account_balance_cards_account_cards'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cards',
            name='card_release',
            field=models.DateField(auto_now=True, verbose_name='Выпуск карты'),
        ),
    ]
