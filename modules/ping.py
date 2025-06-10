import time
import asyncio
from datetime import datetime
from pyrogram import Client, filters
from pyrogram.types import Message

# Add this animation at the top of your file
PING_ANIMATION = [
    "🟥⬜⬜⬜⬜⬜⬜⬜⬜⬜",
    "🟥🟥⬜⬜⬜⬜⬜⬜⬜⬜",
    "🟥🟥🟧⬜⬜⬜⬜⬜⬜⬜",
    "🟥🟥🟧🟧⬜⬜⬜⬜⬜⬜",
    "🟥🟥🟧🟧🟨⬜⬜⬜⬜⬜",
    "🟥🟥🟧🟧🟨🟨⬜⬜⬜⬜",
    "🟥🟥🟧🟧🟨🟨🟩⬜⬜⬜",
    "🟥🟥🟧🟧🟨🟨🟩🟩⬜⬜",
    "🟥🟥🟧🟧🟨🟨🟩🟩🟦⬜",
    "🟥🟥🟧🟧🟨🟨🟩🟩🟦🟦",
    "🟥🟥🟧🟧🟨🟨🟩🟩🟦⬛",
    "🟥🟥🟧🟧🟨🟨🟩🟩⬛⬛",
    "🟥🟥🟧🟧🟨🟨🟩⬛⬛⬛",
    "🟥🟥🟧🟧🟨🟨⬛⬛⬛⬛",
    "🟥🟥🟧🟧🟨⬛⬛⬛⬛⬛",
    "🟥🟥🟧🟧⬛⬛⬛⬛⬛⬛",
    "🟥🟥🟧⬛⬛⬛⬛⬛⬛⬛",
    "🟥🟥⬛⬛⬛⬛⬛⬛⬛⬛",
    "🟥⬛⬛⬛⬛⬛⬛⬛⬛⬛"
]

# Replace your existing ping handler or add this new one
@Client.on_message(filters.command("ping", prefixes=["!", ".", "/"]) & filters.me)
async def animated_ping(client: Client, message: Message):
    start_time = time.time()
    ping_msg = await message.edit("**🚀 Pinging...**")
    
    # Animation loop
    for frame in PING_ANIMATION:
        await ping_msg.edit(f"**{frame}**\n\n`Pinging Moon-Userbot Server...`")
        await asyncio.sleep(0.2)
    
    # Calculate ping time
    end_time = time.time()
    ping_time = round((end_time - start_time) * 1000, 2)
    
    # Final result
    await ping_msg.edit(
        f"**🏓 PONG!**\n"
        f"**⚡ Speed:** `{ping_time} ms`\n"
        f"**🌙 Userbot:** `Moon-Userbot`\n"
        f"**🐍 Python:** `3.11`\n"
        f"**🔥 Pyrogram:** `2.0.0`"
    )
