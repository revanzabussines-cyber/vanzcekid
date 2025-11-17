from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
import os

TOKEN = os.getenv("BOT_TOKEN")

def start(update, context):
    user = update.message.from_user
    user_id = user.id
    chat_id = update.message.chat.id

    keyboard = [
        [InlineKeyboardButton("🔍 Cek ID", callback_data="cek_id")],
        [
            InlineKeyboardButton("💬 Channel", url="https://t.me/VanzDisscusion"),
            InlineKeyboardButton("👥 Group", url="https://t.me/VANZSHOPGROUP"),
        ],
        [InlineKeyboardButton("👨‍💻 Admin", url="https://t.me/VanzzSkyyID")]
    ]

    text = (
        f"👋 Welcome!\n\n"
        f"👤 User ID: `{user_id}`\n"
        f"💬 Chat ID: `{chat_id}`\n\n"
        f"🤖 Bot by @VanzzSkyyID\n"
        f"🛒 Cheapest All Apps: @VanzShopBot"
    )

    update.message.reply_text(text, parse_mode="Markdown",
                              reply_markup=InlineKeyboardMarkup(keyboard))


def button(update, context):
    query = update.callback_query
    user = query.from_user
    user_id = user.id
    chat_id = query.message.chat.id

    text = (
        f"🔍 Cek ID!\n\n"
        f"👤 User ID: `{user_id}`\n"
        f"💬 Chat ID: `{chat_id}`\n\n"
        f"🤖 Bot by @VanzzSkyyID\n"
        f"🛒 Cheapest All Apps: @VanzShopBot"
    )

    query.edit_message_text(text, parse_mode="Markdown")


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, start))
    dp.add_handler(telegram.ext.CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
