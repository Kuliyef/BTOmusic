from pyrogram import Client
import asyncio
from config import SUDO_USERS
from config import PMPERMIT
from pyrogram import filters
from pyrogram.types import Message
from callsmusic.callsmusic import client as USER

PMSET =True
pchats = []

@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
    if PMPERMIT == "ENABLE":
        if PMSET:
            chat_id = message.chat.id
            if chat_id in pchats:
                return
            await USER.send_message(
                message.chat.id,
                "Salam, musiqi asistan xidmətdədir.\n\n ❗️ Əmrlər:\n - Söhbətə icazə yoxdur.\n - Məlumat və Əmrlərim üçün qrup söhbətinizdə **/help** yazsanı. (Asistan şəxsinə məlumat yazmayın.) Musiqi əmrlərini öyrənə bilərsiniz. \n - İstənməyən posta icazə verilmir \n\n 🚨 **Userbot Qrupunuza Qoşulmursa >> Bağlantı ilə dəvət etmə və səsli idarəetmə yetkisini verin. <<**\n\n ⚠️ DİQQƏT: Buraya mesaj göndərirsinizsə. Admin mesajınızı görəcək.\n - Şəxsi məlumatları burada paylaşmayın. (Zəhmət olmasa musiqi botunu şəxsi qruplara aparmayın.) 📚 Məlumat üçün [Developer 🧩](https://t.me/OldDictator) 🇦🇿\n",
            )
            return
 
    

@Client.on_message(filters.command(["/pmpermit"]))
async def bye(client: Client, message: Message):
    if message.from_user.id in SUDO_USERS:
        global PMSET
        text = message.text.split(" ", 1)
        queryy = text[1]
        if queryy == "on":
            PMSET = True
            await message.reply_text("PM İcazə aktivdir")
            return
        if queryy == "off":
            PMSET = None
            await message.reply_text("PM İcazə deaktiv edilib")
            return

@USER.on_message(filters.text & filters.private & filters.me)        
async def autopmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("**Userbot yazışmaları indi uğurludur.**")
        return
    message.continue_propagation()    
    
@USER.on_message(filters.command("a", [".", ""]) & filters.me & filters.private)
async def pmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("Təxminən PM")
        return
    message.continue_propagation()    
    

@USER.on_message(filters.command("da", [".", ""]) & filters.me & filters.private)
async def rmpmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if chat_id in pchats:
        pchats.remove(chat_id)
        await message.reply_text("Bu şəkildə PM")
        return
    message.continue_propagation()
