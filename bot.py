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


def format_main_text(name: str, user_id: int, chat_id: int) -> str:
    return (
        f"👋 Halo **{name}**!\n\n"
        f"👤 User ID: `{user_id}`\n"
        f"💬 Chat ID: `{chat_id}`\n\n"
        f"🤖 Bot by **@VanzzSkyyID**\n"
        f"🛒 Cheapest All Apps → **@VanzShopBot**"
    )


def format_cekid_text(name: str, user_id: int, chat_id: int) -> str:
    return (
        f"🔍 **ID Detail untuk {name}:**\n\n"
        f"👤 User ID: `{user_id}`\n"
        f"💬 Chat ID: `{chat_id}`\n\n"
        f"🤖 Bot by @VanzzSkyyID\n"
        f"🛒 Cheapest All Apps → @VanzShopBot"
    )


# ========== /start ==========
@dp.message(CommandStart())
async def cmd_start(message: Message):
    user = message.from_user
    chat = message.chat

    name = user.first_name or "User"
    user_id = user.id
    chat_id = chat.id

    text = format_main_text(name, user_id, chat_id)
    await message.answer(
        text,
        reply_markup=get_keyboard(),
        parse_mode="Markdown",
    )


# ========== chat apapun (teks) ==========
@dp.message(F.text & ~F.via_bot)
async def any_text(message: Message):
    # sama aja kayak /start → auto tampil info ID
    await cmd_start(message)


# ========== tombol "Cek ID" ==========
@dp.callback_query(F.data == "cek_id")
async def cb_cek_id(callback_query: CallbackQuery):
    user = callback_query.from_user
    chat = callback_query.message.chat

    name = user.first_name or "User"
    user_id = user.id
    chat_id = chat.id

    text = format_cekid_text(name, user_id, chat_id)

    await callback_query.message.edit_text(
        text,
        parse_mode="Markdown",
        reply_markup=get_keyboard(),
    )
    await callback_query.answer()  # tutup loading di Telegram


async def main():
    if not TOKEN:
        raise RuntimeError("ENV BOT_TOKEN belum di-set!")

    bot = Bot(TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
