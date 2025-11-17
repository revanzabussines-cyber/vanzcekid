from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# ==============================
#  HANDLERS
# ==============================

async def send_welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    chat = update.effective_chat

    user_id = user.id
    chat_id = chat.id

    # Tombol
    keyboard = [
        [InlineKeyboardButton("🔍 Cek ID", callback_data="cek_id")],
        [
            InlineKeyboardButton("💬 Channel", url="https://t.me/VanzDisscusion"),
            InlineKeyboardButton("👥 Group", url="https://t.me/VANZSHOPGROUP"),
        ],
        [InlineKeyboardButton("👨‍💻 Admin", url="https://t.me/VanzzSkyyID")]
    ]

    text = (
        f"👋 **Welcome!**\n\n"
        f"**ID kamu:** `{user_id}`\n"
        f"**Chat ID:** `{chat_id}`\n\n"
        f"🤖 Bot by **@VanzzSkyyID**\n"
        f"🛒 Cheapest All Apps: **@VanzShopBot**"
    )

    await update.message.reply_markdown(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def callback_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
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


# ==============================
#  MAIN
# ==============================

async def main():
    app = ApplicationBuilder().token("YOUR_BOT_TOKEN").build()

    # /start
    app.add_handler(CommandHandler("start", send_welcome))

    # kalau user chat apa saja → tetap kirim info ID
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, send_welcome))

    # button callback
    app.add_handler(MessageHandler(filters.COMMAND, send_welcome))
    app.add_handler(telegram.ext.CallbackQueryHandler(callback_button))

    print("BOT READY...")
    await app.run_polling()

import asyncio
asyncio.run(main())
