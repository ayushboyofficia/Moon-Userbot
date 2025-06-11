from pyrogram import Client, filters
import random

@Client.on_message(filters.command("hack") & filters.me)
async def fake_hack(client, message):
    if not message.reply_to_message:
        return await message.reply("Reply to someone to fake hack them!")
    
    user = message.reply_to_message.from_user
    hacking_steps = [
        f"📡 {user.first_name}'s phone location traced!",
        f"💻 Bypassing 2FA security...",
        f"🔑 Password cracked: 'iloveyou123'",
        f"📂 Accessing gallery... nudes found! 😈",
        f"💰 Bank account emptied! ₹69,420 transferred!",
        f"✅ Successfully hacked {user.mention} !"
    ]
    
    msg = await message.reply("🚀 Starting hack...")
    
    for step in hacking_steps:
        await asyncio.sleep(2)
        await msg.edit(step)
    
    await msg.reply("😂 Just kidding! Noob saala!")
