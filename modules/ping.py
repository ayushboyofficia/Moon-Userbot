#  Moon-Userbot - telegram userbot
#  Copyright (C) 2020-present Moon Userbot Organization
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.

#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.

#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

import time
import asyncio
from datetime import datetime
from pyrogram import Client, filters
from pyrogram.types import Message

# Ping Animation Characters
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

@Client.on_message(filters.command("ping", prefixes=["!", ".", "/"]) & filters.me)
async def animated_ping(client: Client, message: Message):
    """Animated ping command with colorful loading bar"""
    start_time = time.time()
    
    # Initial ping message
    ping_msg = await message.edit("**🚀 Pinging...**")
    
    # Animation loop
    for frame in PING_ANIMATION:
        await ping_msg.edit(f"**{frame}**\n\n`Pinging Moon-Userbot Server...`")
        await asyncio.sleep(0.2)
    
    # Calculate ping time
    end_time = time.time()
    ping_time = round((end_time - start_time) * 1000, 2)
    
    # Final result with colorful formatting
    await ping_msg.edit(
        f"**🏓 PONG!**\n"
        f"**⚡ Speed:** `{ping_time} ms`\n"
        f"**🌙 Userbot:** `Moon-Userbot`\n"
        f"**🐍 Python:** `3.11`\n"
        f"**🔥 Pyrogram:** `2.0.0`"
    )
