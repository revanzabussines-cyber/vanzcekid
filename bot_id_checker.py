from telegram import (
    Update,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters
)


# ==============================
#  RESPON WELCOME + ID
# ==============================
async def send_welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    chat = update.effective_chat
    
    user_id = user.id
    chat_id = chat.id

    # tombol
    keyboard = [
        [InlineKeyboardButton("🔍 Cek ID", callback_data="cek_id")],
        [
            InlineKeyboardButton("💬 Channel", url="https://t.me/VanzDisscusion"),
            InlineKeyboardButton("👥 Group", url="https://t.me/VANZSHOPGROUP"),
        ],
        [InlineKeyboardButton("👨‍💻 Admin", url="https://t.me/VanzzSkyyID")]
    ]

    teks = (
        f"👋 **Welcome!**\n\n"
        f"👤 User ID: `{user_id}`\n"
        f"💬 Chat ID: `{chat_id}`\n\n"
        f"🤖 Bot by **@VanzzSkyyID**\n"
        f"🛒 Cheapest All Apps: **@VanzShopBot**"
    )

    await update.message.reply_markdown(
        teks,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# ==============================
#  TOMBOL CALLBACK
# ==============================
async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user = query.from_user
    user_id = user.id
    chat_id = query.message.chat.id

    teks = (
        f"🔍 **Cek ID Berhasil!**\n\n"
        f"👤 User ID: `{user_id}`\n"
        f"💬 Chat ID: `{chat_id}`\n\n"
        f"🤖 Bot by @VanzzSkyyID\n"
        f"🛒 Cheapest All Apps: @VanzShopBot"
    )

    await query.edit_message_text(
        text=teks,
        parse_mode="Markdown"
    )


# ==============================
#  MAIN
# ==============================
def main():
    app = ApplicationBuilder().token("YOUR_BOT_TOKEN").build()

    # /start
    app.add_handler(CommandHandler("start", send_welcome))

    # chat apapun tetap munculin ID
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, send_welcome))

    # callback tombol (INI PENTING!)
    app.add_handler(CallbackQueryHandler(button_callback))

    print("BOT RUNNING...")
    app.run_polling()


if __name__ == "__main__":
    main()
