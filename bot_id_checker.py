import os
from telegram import Update
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackContext,
    MessageHandler,
    Filters,
)

# ==========================
# CONFIG
# ==========================

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is missing. Please set it in your environment variables.")

OWNER_USERNAME = "@VanzzSkyyID"
SHOP_BOT = "@VanzShopBot"

CREDIT_TEXT = f"\n\n———\n🤖 Bot by {OWNER_USERNAME}\n🛒 Cheapest All Apps: {SHOP_BOT}"


# ==========================
# COMMAND HANDLERS
# ==========================

def start(update: Update, context: CallbackContext):
    user = update.effective_user

    text = (
        "👋 Welcome!\n\n"
        "This bot helps you **check Telegram IDs** easily.\n\n"
        "✅ Features:\n"
        "• Get **your own user ID**\n"
        "• Get **chat / group / channel ID**\n"
        "• Get **ID of someone you reply to**\n\n"
        "🔧 How to use:\n"
        "• Send /id in private chat\n"
        "• Use /id in a group to get the group ID\n"
        "• Reply to someone's message and send /id to get their ID\n"
        f"{CREDIT_TEXT}"
    )

    update.message.reply_text(text, parse_mode="Markdown")


def id_command(update: Update, context: CallbackContext):
    message = update.message
    user = update.effective_user
    chat = update.effective_chat

    lines = []

    # Your info
    lines.append("🧾 *Your info*")
    lines.append(f"• User ID: `{user.id}`")
    if user.username:
        lines.append(f"• Username: @{user.username}")
    if user.full_name:
        lines.append(f"• Name: {user.full_name}")

    # Chat info
    lines.append("\n💬 *Chat info*")
    lines.append(f"• Chat ID: `{chat.id}`")
    lines.append(f"• Chat type: `{chat.type}`")
    if chat.title:
        lines.append(f"• Chat title: {chat.title}")

    # If reply to someone → show their ID
    if message.reply_to_message:
        replied_user = message.reply_to_message.from_user
        lines.append("\n👥 *Replied user*")
        lines.append(f"• User ID: `{replied_user.id}`")
        if replied_user.username:
            lines.append(f"• Username: @{replied_user.username}")
        if replied_user.full_name:
            lines.append(f"• Name: {replied_user.full_name}")

    # If forwarded message → original sender
    if message.forward_from:
        fwd_user = message.forward_from
        lines.append("\n📨 *Forwarded from*")
        lines.append(f"• User ID: `{fwd_user.id}`")
        if fwd_user.username:
            lines.append(f"• Username: @{fwd_user.username}")
        if fwd_user.full_name:
            lines.append(f"• Name: {fwd_user.full_name}")

    # Join & send
    text = "\n".join(lines) + CREDIT_TEXT

    message.reply_text(text, parse_mode="Markdown")


def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "I only support /start and /id.\n"
        "Use /id to check IDs." + CREDIT_TEXT
    )


# ==========================
# MAIN
# ==========================

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("id", id_command))

    # Optional: reply something if user types random command
    dp.add_handler(MessageHandler(Filters.command, unknown))

    print("✅ ID Checker Bot is running...")
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
