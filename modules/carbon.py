import asyncio
import sys
from pathlib import Path
from io import BytesIO
import aiohttp
from pyrogram import Client, filters
from pyrogram.types import Message

# Path सेटअप
sys.path.append(str(Path(__file__).parent.parent.parent))
from utils.helpers import edit_or_reply
from config import Config

hl = Config.CMD_HANDLER

async def make_carbon(code):
    url = "https://carbonara.solopov.dev/api/cook"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json={"code": code}) as resp:
            image = BytesIO(await resp.read())
            image.name = "carbon.png"
            return image

@Client.on_message(filters.command("carbon", hl) & filters.me)
async def carbon_func(client: Client, message: Message):
    text = " ".join(message.command[1:]) if len(message.command) > 1 else None
    if message.reply_to_message:
        text = message.reply_to_message.text or message.reply_to_message.caption
    if not text:
        return await edit_or_reply(message, "Please provide text or reply to a message!")
    
    msg = await edit_or_reply(message, "Creating Carbon...")
    try:
        carbon = await make_carbon(text)
        await msg.edit("Uploading...")
        await client.send_photo(
            message.chat.id,
            carbon,
            caption=f"Carbonized by {client.me.mention}",
            reply_to_message_id=message.reply_to_message.id if message.reply_to_message else None
        )
        await msg.delete()
    except Exception as e:
        await msg.edit(f"Error: {str(e)}")
    finally:
        if 'carbon' in locals():
            carbon.close()
