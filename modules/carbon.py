import asyncio
import aiohttp
from io import BytesIO
from pyrogram import Client, filters
from pyrogram.types import Message

async def make_carbon(code):
    """Carbon.sh API का उपयोग करके कोड इमेज बनाता है"""
    url = "https://carbonara.solopov.dev/api/cook"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json={"code": code}) as resp:
            image = BytesIO(await resp.read())
            image.name = "carbon.png"
            return image

@Client.on_message(filters.command("carbon") & filters.me)
async def carbon_func(client: Client, message: Message):
    # टेक्स्ट निकालें (रिप्लाई या कमांड आर्ग्युमेंट से)
    text = message.text.split(" ", 1)[1] if len(message.command) > 1 else None
    if message.reply_to_message:
        text = message.reply_to_message.text or message.reply_to_message.caption
    
    if not text:
        await message.reply("कृपया कोई टेक्स्ट दें या किसी मैसेज को रिप्लाई करें!")
        return

    processing_msg = await message.reply("कार्बन इमेज बना रहा हूँ...")
    
    try:
        carbon_image = await make_carbon(text)
        await message.reply_photo(
            carbon_image,
            caption="यहाँ आपका कार्बन इमेज है!"
        )
    except Exception as e:
        await message.reply(f"त्रुटि: {str(e)}")
    finally:
        await processing_msg.delete()
        if 'carbon_image' in locals():
            carbon_image.close()
