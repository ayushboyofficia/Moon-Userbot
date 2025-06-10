import asyncio
from io import BytesIO

from pyrogram import Client, filters
from pyrogram.types import Message

from config import CMD_HANDLER
from config import SUDO_USERS
from Moon import aiosession
from Moon.helpers.basic import edit_or_reply
from Moon.helpers.PyroHelpers import ReplyCheck

from .help import *

async def make_carbon(code):
    url = "https://carbonara.solopov.dev/api/cook"
    async with aiosession.post(url, json={"code": code}) as resp:
        image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image

@Client.on_message(
    filters.command(["carbon"], CMD_HANDLER) & (filters.me | filters.user(SUDO_USERS))
)
async def carbon_func(client: Client, message: Message):
    text = (
        message.text.split(None, 1)[1]
        if len(message.command) != 1
        else None
    )
    if message.reply_to_message:
        text = message.reply_to_message.text or message.reply_to_message.caption
    if not text:
        return await message.delete()
    Moon = await edit_or_reply(message, "`Preparing Carbon...`")
    carbon = await make_carbon(text)
    await Moon.edit("`Uploading...`")
    await asyncio.gather(
        Moon.delete(),
        client.send_photo(
            message.chat.id,
            carbon,
            caption=f"**Carbonized by** {client.me.mention}",
            reply_to_message_id=ReplyCheck(message),
        ),
    )
    carbon.close()

add_command_help(
    "•─╼⃝𖠁 Carbon",
    [
        [f"{CMD_HANDLER}carbon <reply/text>", "Creates a carbonized image of the provided text or replied message."],
    ],
)
