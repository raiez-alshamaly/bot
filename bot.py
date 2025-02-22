import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
from config import TOKEN
from database import session, User

# إعداد تسجيل السجلات
logging.basicConfig(level=logging.INFO)

# تهيئة البوت والموزع (Dispatcher)
bot = Bot(token=TOKEN)
dp = Dispatcher()

# 📌 أمر بدء البوت
@dp.message(Command("start"))
async def start_command(message: Message):
    user = session.query(User).filter_by(telegram_id=message.from_user.id).first()

    if not user:
        new_user = User(
            telegram_id=message.from_user.id,
            username=message.from_user.username,
            password="hashed_password",
            referral_link=f"https://t.me/YOUR_BOT_USERNAME?start={message.from_user.id}",
            balance=0.00
        )
        session.add(new_user)
        session.commit()
        await message.answer(f"🎉 مرحباً {message.from_user.username}!\nتم تسجيلك في البوت ✅")
    else:
        await message.answer(f"👋 مرحباً مجدداً {message.from_user.username}!\nرصيدك الحالي: {user.balance}$")

# 📌 تشغيل البوت
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
