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

TOKEN = os.getenv("BOT_TOKEN")


# ========================
# START COMMAND
# ========================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    chat = update.effective_chat

    name = user.first_name
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
        f"👋 Halo **{name}**!\n\n"
        f"👤 User ID: `{user_id}`\n"
        f"💬 Chat ID: `{chat_id}`\n\n"
        f"🤖 Bot by **@VanzzSkyyID**\n"
        f"🛒 Cheapest All Apps → **@VanzShopBot**"
    )

    if update.message:
        await update.message.reply_markdown(
            text,
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


# ========================
# CALLBACK BUTTON
# ========================
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user = query.from_user
    name = user.first_name
    user_id = user.id
    chat_id = query.message.chat.id

    text = (
        f"🔍 **ID Detail untuk {name}:**\n\n"
        f"👤 User ID: `{user_id}`\n"
        f"💬 Chat ID: `{chat_id}`\n\n"
        f"🤖 Bot by @VanzzSkyyID\n"
        f"🛒 Cheapest All Apps → @VanzShopBot"
    )

    await query.edit_message_text(text, parse_mode="Markdown")


# ========================
# AUTO RESPON CHAT APA SAJA
# ========================
async def auto_show_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await start(update, context)


# ========================
# MAIN APP
# ========================
def main():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN belum di-set di Railway")

    app = ApplicationBuilder().token(TOKEN).build()

    # command
    app.add_handler(CommandHandler("start", start))

    # tombol callback
    app.add_handler(CallbackQueryHandler(button))

    # chat apa pun → tampilkan info
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_show_id))

    print("BOT RUNNING...")
    app.run_polling()


if __name__ == "__main__":
    main()
