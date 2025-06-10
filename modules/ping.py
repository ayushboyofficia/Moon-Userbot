import time
from datetime import datetime
from pyrogram import Client, filters
from pyrogram.types import Message
from Moon.helpers.basic import edit_or_reply
from config import HANDLER as hl

START_TIME = datetime.utcnow()

@Client.on_message(filters.command("ping", hl) & filters.me)
async def ping_me(client: Client, message: Message):
    start = time.time()
    moon = await edit_or_reply(message, "`Pong!`")
    end = time.time()
    duration = (end - start) * 1000
    
    uptime = datetime.utcnow() - START_TIME
    uptime_seconds = uptime.total_seconds()
    
    await moon.edit(
        f"🌙 **Moon Userbot Ping**\n"
        f"• **Ping:** `{duration:.2f}ms`\n"
        f"• **Uptime:** `{uptime_seconds:.2f}s`\n"
        f"• **Version:** `1.0`"
    )
