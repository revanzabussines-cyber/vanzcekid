import os
import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from aiogram.filters import CommandStart

TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher()


# ====================== KEYBOARD ======================
def get_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🔍 Cek ID", callback_data="cek_id")],
            [
                InlineKeyboardButton(
                    text="💬 Channel", url="https://t.me/VanzDisscusion"
                ),
                InlineKeyboardButton(
                    text="👥 Group", url="https://t.me/VANZSHOPGROUP"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="👨‍💻 Admin", url="https://t.me/VanzzSkyyID"
                )
            ],
        ]
    )


# ====================== TEXT TEMPLATES ======================
def format_main_text(name: str, user_id: int, chat_id: int) -> str:
    return (
        f"👋 Halo **{name}**!\n\n"
        f"✨ Selamat datang di *VanzShop ID Checker*\n\n"
        f"Bot ini memudahkan kamu untuk:\n"
        f"• 👤 Melihat User ID\n"
        f"• 💬 Mengetahui Chat / Group ID\n"
        f"• ↩️ Melihat ID dari pesan yang kamu reply\n\n"
        f"📌 Informasi kamu:\n"
        f"• 👤 User ID: `{user_id}`\n"
        f"• 💬 Chat ID: `{chat_id}`\n\n"
        f"🤖 Bot by **@VanzzSkyyID**\n"
        f"🛒 Cheapest All Apps → **@VanzShopBot**"
    )


def format_cekid_text(name: str, user_id: int, chat_id: int) -> str:
    return (
        f"🔍 **Cek ID untuk {name}:**\n\n"
        f"• 👤 User ID: `{user_id}`\n"
        f"• 💬 Chat ID: `{chat_id}`\n\n"
        f"🤖 Bot by @VanzzSkyyID\n"
        f"🛒 Cheapest All Apps → @VanzShopBot"
    )


# ====================== HANDLERS ======================

@dp.message(CommandStart())
async def start(message: Message):
    user = message.from_user
    chat = message.chat

    name = user.first_name or "User"
    user_id = user.id
    chat_id = chat.id

    await message.answer(
        format_main_text(name, user_id, chat_id),
        reply_markup=get_keyboard(),
        parse_mode="Markdown",
    )


@dp.message(F.text & ~F.via_bot)
async def auto_show(message: Message):
    await start(message)


@dp.callback_query(F.data == "cek_id")
async def callback_cekid(callback_query: CallbackQuery):
    user = callback_query.from_user
    chat = callback_query.message.chat

    name = user.first_name or "User"
    user_id = user.id
    chat_id = chat.id

    await callback_query.message.edit_text(
        format_cekid_text(name, user_id, chat_id),
        parse_mode="Markdown",
        reply_markup=get_keyboard(),
    )

    await callback_query.answer()


# ====================== MAIN ======================
async def main():
    if not TOKEN:
        raise RuntimeError("ENV BOT_TOKEN belum di-set di Railway!")

    bot = Bot(TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
