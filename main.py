from aiogram import executor
from aiogram.types import *

import info_handler
import keyboard as kb
from config import dp, bot


@dp.message_handler(commands=["start"])
async def start_message(msg: Message):
    await msg.reply(
        text="Привет! Я отслеживаю статистику заражения 2019-nCoV.\n"
             "Используйте /menu чтобы получить всю информацию.")


@dp.message_handler(commands=["menu"])
async def menu_message(msg: Message):
    await msg.reply(
        text="Используйте *кнопки ниже*:",
        reply_markup=kb.main_menu(),
    )


@dp.callback_query_handler(lambda _call: True)
async def handle_callbacks(call: CallbackQuery):
    """Отлавливаем кэллбэки телеграма."""
    chat_id = call.message.chat.id
    username = call.from_user.username

    if call.data == "current_stats":
        info = info_handler.get_main_info()
        await call.message.edit_text(
            f"*Статистика 2019-nCoV*:\n\n"
            f"Зараженных ☣️: *{info['Infected']}*\n\n"
            f"На подозрении ❓: *{info['Possible']}*\n\n"
            f"На карантине ☢️: *{info['Quarantine']} ({info['Quarantined_Cities']} городов)\n\n*"
            f"Вылечившихся 💊: *{info['Recovered']}*\n\n"
            f"Смерти ☠️: *{info['Deaths']}*\n\n"
            f"_Смертность составляет {info['Death_Rate']}%_\n"
            f"Последнее обновление: *{info['Date']} MSK*",
            reply_markup=kb.main_menu(),
        )
        await call.answer()
    elif call.data == "quarantined_cities":
        table = info_handler.get_table_cities()
        answer_message = "*Города на карантине*\n(Город\t\t|\t\t дата закрытия\t\t|\t\tНаселение)__\n\n"
        for i in range(len(table)-1):
            answer_message += f"{table[i][0]} - {table[i][1]} - {table[i][2]}\n"
        await call.message.edit_text(
            answer_message+"__",
            reply_markup=kb.info_menu())
        await call.answer()
    elif call.data == "disease_forecast":
        table = info_handler.disease_forecast()
        answer_message = "*Прогноз заражения по Китаю на ближайшие 5 дней:*\n\n" \
                         "*Дата*              |\t\t\t*Кол-во инфицированных*\n"
        for i in range(len(table)):
            answer_message += f"{table[i][0]}\t\t\t|\t\t\t{table[i][1]}\n"
        answer_message = answer_message.replace("(Прогноз)", "`(Прогноз)`")
        await call.message.edit_text(answer_message +
                                     "\n\n_На основании данных статистики за последние 5 дней по Китаю (текущий день не учитывается)"
                                     "\nСтатистика актуальна при среднем модификаторе заражения в 1.304180_",
                                     reply_markup=kb.main_menu())
        await call.answer()
    elif call.data == "back_to_home":
        await call.message.edit_text("Используйте *кнопки ниже*:",
                               reply_markup=kb.main_menu())
        await call.answer()


@dp.inline_handler()
async def inline_stats(inline_query: InlineQuery):
    info = info_handler.get_main_info()
    text =  (f"*Статистика 2019-nCoV*:\n\n"
    f"Зараженных ☣️: *{info['Infected']}*\n\n"
    f"На подозрении ❓: *{info['Possible']}*\n\n"
    f"На карантине ☢️: *{info['Quarantine']} ({info['Quarantined_Cities']} городов)\n\n*"
    f"Вылечившихся 💊: *{info['Recovered']}*\n\n"
    f"Смерти ☠️: *{info['Deaths']}*\n\n"
    f"_Смертность составляет {info['Death_Rate']}%_\n"
             
    f"Последнее обновление: *{info['Date']} MSK*")
    input_content = InputTextMessageContent(text)
    item = InlineQueryResultArticle(
        id="1", title="2019-nCoV stats", input_message_content=input_content
    )
    await bot.answer_inline_query(inline_query.id, results=[item], cache_time=1)


# @dp.errors_handler()
# async def error_handler():



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
