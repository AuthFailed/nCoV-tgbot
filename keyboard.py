from aiogram.types.inline_keyboard import *

Btn = InlineKeyboardButton


def main_menu():
    kb = InlineKeyboardMarkup()

    current_status = Btn(text="Стат. на данный момент",
                         callback_data="current_stats")
    country_stats = Btn(text="Города на карантине",
                        callback_data="quarantined_cities")
    national_infections = Btn(text="Заражения по странам",
                              callback_data="national_infections")
    disease_forecast = Btn(text="Прогноз заболеваемости",
                           callback_data="disease_forecast")
    kb.add(current_status)
    kb.add(disease_forecast)
    kb.add(country_stats, national_infections)
    return kb
