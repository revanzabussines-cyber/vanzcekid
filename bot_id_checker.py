import os
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters,
)

TOKEN = os.getenv("BOT_TOKEN")  # set di Railway

# ========== RESPON WELCOME / INFO ID ==========
async def send_welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    chat = update.effective_chat

    user_id = user.id
    chat_id = chat.id

    keyboard = [
        [InlineKeyboardButton("🔍 Cek ID", callback_data="cek_id")],
        [
            InlineKeyboardButton("💬 Channel", url="https://t.me/VanzDisscusion"),
            InlineKeyboardButton("👥 Group", url="https://t.me/VANZSHOPGROUP"),
        ],
        [InlineKeyboardButton("👨‍💻 Admin", url="https://t.me/VanzzSkyyID")],
    ]

    text = (
        f"👋 **Welcome!**\n\n"
        f"👤 User ID: `{user_id}`\n"
        f"💬 Chat ID: `{chat_id}`\n\n"
        f"🤖 Bot by **@VanzzSkyyID**\n"
        f"🛒 Cheapest All Apps: **@VanzShopBot**"
    )

    # kadang update.message bisa None (misal dari callback), jadi dicek dulu
    if update.message:
        await update.message.reply_markdown(
            text,
            reply_markup=InlineKeyboardMarkup(keyboard),
        )


# ========== CALLBACK TOMBOL ==========
async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user = query.from_user
    user_id = user.id
    chat_id = query.message.chat.id

    text = (
        f"🔍 **Cek ID Berhasil!**\n\n"
        f"👤 User ID: `{user_id}`\n"
        f"💬 Chat ID: `{chat_id}`\n\n"
        f"🤖 Bot by @VanzzSkyyID\n"
        f"🛒 Cheapest All Apps: @VanzShopBot"
    )

    await query.edit_message_text(
        text=text,
        parse_mode="Markdown"
    )


# ========== MAIN ==========
def main():
    if not TOKEN:
        raise RuntimeError("ENV BOT_TOKEN belum di-set di Railway!")

    app = ApplicationBuilder().token(TOKEN).build()

    # /start → kirim ID + tombol
    app.add_handler(CommandHandler("start", send_welcome))

    # chat teks apa pun (non-command) → kirim ID + tombol juga
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, send_welcome))

    # handler buat tombol inline
    app.add_handler(CallbackQueryHandler(button_callback))

    print("BOT RUNNING...")
    app.run_polling()


if __name__ == "__main__":
    main()
