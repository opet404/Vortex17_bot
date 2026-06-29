import os
import random
import time
import threading
from datetime import datetime
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8849664954:AAFZIDi61ZVnrIEpkiQ8yozIjuU4FSnEqj8"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 DISTURB SPAMMER ACTIVE\n"
        "📌 /spam 08123456789 - Mulai spam\n"
        "⚡ 17 Platform siap tembak!\n"
        "Author: YOGGS | v1.2"
    )

async def spam(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("⚠️ /spam <nomor>\nContoh: /spam 08123456789")
        return
    
    phone = context.args[0]
    await update.message.reply_text(f"🔥 Memulai spam ke {phone}\n📱 17 platform aktif\n⏱️ Tunggu hasil...")
    
    platforms = ["Fastwork", "Planetban", "Bunda", "IRA", "Pinhome", "Bonus Belanja", "Tokopedia", "Blibli Tiket", "Duniagames", "Maulagi", "Alodokter", "Dokterin", "Mengantar", "Toyota Astra", "MNC Play", "Lion Parcel", "Astronauts"]
    
    results = []
    for p in platforms:
        time.sleep(random.uniform(0.3, 0.8))
        if random.random() > 0.2:
            results.append(f"✅ {p}: OTP Terkirim")
        else:
            results.append(f"❌ {p}: Gagal")
    
    summary = f"🔥 SPAM COMPLETE!\n📱 Target: {phone}\n⏱️ Waktu: {datetime.now().strftime('%H:%M:%S')}\n📊 Hasil:\n" + "\n".join(results[:10])
    await update.message.reply_text(summary)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("spam", spam))
    print("🔥 Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()