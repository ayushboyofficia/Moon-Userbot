from pyrogram import Client, filters
from pyrogram.types import Message
import random

# Shayari Database
SHAYARI_DB = [
    "दिल तोड़ने वालों को मिलते रहेंगे सज्जन,\nहम जैसे ही किसी के हो जाएंगे, खुदा का शुक्र अदा करेंगे।",
    "मोहब्बत की राह में चलना सीख लो,\nजिंदगी भर के लिए याद आऊंगा मैं तुम्हें।",
    "तुम्हारी याद के सिवा कुछ भी नहीं,\nतुम्हारे बिना जिंदगी अधूरी सी लगती है।",
    "ख्वाबों में भी तुम आओ तो डर लगता है,\nवरना हम तो तन्हाई में भी साथ रहते हैं।"
]

@Client.on_message(filters.command("shayari", prefixes=["!", ".", "/"]) & filters.me)
async def shayari_handler(client: Client, message: Message):
    """Random Shayari भेजता है"""
    random_shayari = random.choice(SHAYARI_DB)
    await message.edit(random_shayari)

@Client.on_message(filters.command("addshayari", prefixes=["!", ".", "/"]) & filters.user(SUDO_USERS))
async def add_shayari_handler(client: Client, message: Message):
    """नई Shayari जोड़ता है (सिर्फ Sudo Users)"""
    if len(message.command) < 2:
        await message.edit("Usage: `.addshayari Your new shayari text`")
        return
    
    new_shayari = " ".join(message.command[1:])
    SHAYARI_DB.append(new_shayari)
    await message.edit(f"✅ Shayari added successfully!\nTotal shayaris now: {len(SHAYARI_DB)}")
