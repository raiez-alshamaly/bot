import os

TOKEN = os.getenv("6528215814:AAE8RxzwmBjWw2ngR35gAdVdLPOKd7mFKHU")  # توكن بوت تيليغرام
DB_URL = os.getenv("mysql://root:NrvdQyzQmlpuPeiCIiZRfzituhqgRoCu@shinkansen.proxy.rlwy.net:11793/railway")  # رابط قاعدة بيانات MySQL

if not DB_URL:
    raise ValueError("❌ خطأ: لم يتم تعيين متغير البيئة DB_URL بشكل صحيح!")

# مثال على DB_URL المطلوب:
# mysql+mysqlconnector://username:password@localhost:3306/telegram_bot_db
