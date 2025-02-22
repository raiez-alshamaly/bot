import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from config import TOKEN
from database import session, User, Transaction

# تفعيل السجلات
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# 📌 أمر بدء البوت
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
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
        await message.reply(f"🎉 مرحباً {message.from_user.username}!\nتم تسجيلك في البوت ✅")

    else:
        await message.reply(f"👋 مرحباً مجدداً {message.from_user.username}!\nرصيدك الحالي: {user.balance}$")

# 📌 أمر شحن الرصيد
@dp.message_handler(commands=['charge'])
async def charge_command(message: types.Message):
    user = session.query(User).filter_by(telegram_id=message.from_user.id).first()
    
    if not user:
        await message.reply("❌ يجب عليك التسجيل أولاً باستخدام /start")
        return

    await message.reply("💳 أرسل المبلغ وطريقة الدفع وسيتم مراجعته.")

# 📌 أمر طلب السحب
@dp.message_handler(commands=['withdraw'])
async def withdraw_command(message: types.Message):
    user = session.query(User).filter_by(telegram_id=message.from_user.id).first()
    
    if not user:
        await message.reply("❌ يجب عليك التسجيل أولاً باستخدام /start")
        return

    await message.reply("🚀 أدخل المبلغ المطلوب سحبه.")

# 📌 أمر عرض الرصيد
@dp.message_handler(commands=['balance'])
async def balance_command(message: types.Message):
    user = session.query(User).filter_by(telegram_id=message.from_user.id).first()
    
    if not user:
        await message.reply("❌ يجب عليك التسجيل أولاً باستخدام /start")
        return

    await message.reply(f"💰 رصيدك الحالي: {user.balance}$")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
