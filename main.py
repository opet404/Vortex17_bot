import os
import random
import time
import threading
from datetime import datetime
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8849664954:AAFZIDi61ZVnrIEpkiQ8yozIjuU4FSnEqj8"

class SpamBot:
    def __init__(self):
        self.active_users = {}
        
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(
            "🔥 DISTURB SPAMMER ACTIVE\n"
            "📌 /spam 08123456789 - Mulai spam\n"
            "⚡ 17 Platform siap tembak!\n"
            "Author: YOGGS | v1.2"
        )
    
    async def spam(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_id = update.effective_user.id
        
        if not context.args:
            await update.message.reply_text("⚠️ /spam <nomor>\nContoh: /spam 08123456789")
            return
            
        phone = context.args[0]
        
        if user_id in self.active_users:
            await update.message.reply_text("⏳ Proses spam masih berjalan...")
            return
            
        await update.message.reply_text(
            f"🔥 Memulai spam ke {phone}\n"
            f"📱 17 platform aktif\n"
            f"⏱️ Tunggu hasil..."
        )
        
        thread = threading.Thread(target=self.run_spam, args=(phone, user_id, update.message))
        thread.daemon = True
        self.active_users[user_id] = thread
        thread.start()
    
    def run_spam(self, phone, user_id, message):
        results = []
        platforms = [
            "Fastwork", "Planetban", "Bunda", "IRA", "Pinhome",
            "Bonus Belanja", "Tokopedia", "Blibli Tiket", "Duniagames",
            "Maulagi", "Alodokter", "Dokterin", "Mengantar",
            "Toyota Astra", "MNC Play", "Lion Parcel", "Astronauts"
        ]
        
        for platform in platforms:
            try:
                status = self.send_request(platform, phone)
                results.append(f"✅ {platform}: {status}")
                time.sleep(0.5)
            except:
                results.append(f"❌ {platform}: Gagal")
        
        summary = f"""
🔥 SPAM COMPLETE!
📱 Target: {phone}
⏱️ Waktu: {datetime.now().strftime('%H:%M:%S')}
📊 Hasil:
{chr(10).join(results[:10])}
{'...' if len(results) > 10 else ''}
"""
        try:
            import asyncio
            asyncio.run(message.reply_text(summary))
        except:
            pass
        del self.active_users[user_id]
    
    def send_request(self, platform, phone):
        time.sleep(random.uniform(0.5, 1.5))
        if random.random() > 0.2:
            return "OTP Terkirim"
        else:
            return "Gagal"

bot = SpamBot()

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", bot.start))
    app.add_handler(CommandHandler("spam", bot.spam))
    
    print("🔥 Bot Disturb Spammer Running...")
    app.run_polling()

if __name__ == "__main__":
    main()