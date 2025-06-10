# MIT License
# Copyright (c) 2025 Moon-Userbot
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from utils.misc import modules_help, prefix

@Client.on_message(filters.command("hang", prefix) & filters.me)
async def hang_command(client: Client, message: Message):
    args = message.text.split()
    
    # Check if count is provided
    if len(args) < 2:
        await message.reply_text(f"Usage: {prefix}hang <count>")
        return
    
    # Check if chat is protected (optional, adjust based on your setup)
    protected_groups = []  # Add protected group IDs here if needed
    if message.chat.id in protected_groups:
        await message.reply_text("This group is protected and cannot be spammed! 🛡️")
        return
    
    try:
        count = int(args[1])
        if count <= 0:
            await message.reply_text("Count must be a positive integer.")
            return
        if count > 50:  # Optional: Limit to prevent abuse
            await message.reply_text("Count cannot exceed 50 to avoid flooding.")
            return
    except ValueError:
        await message.reply_text("Please provide a valid number for count.")
        return
    
    # Define the spam message
    spam_message = "😈꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰"  # Customize as needed
    
    # Send spam messages with delay
    for _ in range(count):
        await client.send_message(message.chat.id, spam_message)
        await asyncio.sleep(0.3)  # 0.3 seconds delay to avoid rate limits

# Add command to help menu
modules_help["hang"] = {
    "hang [count]": "Spams the chat with a message [count] times."
}
