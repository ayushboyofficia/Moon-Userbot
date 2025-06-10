from pyrogram import Client, filters
from Moon.helpers.basic import edit_or_reply
from config import HANDLER as hl

FONT_STYLES = {
    'bold': '𝗧𝗵𝗶𝘀 𝗶𝘀 𝗯𝗼𝗹𝗱 𝘁𝗲𝘅𝘁',
    'italic': '𝙏𝙝𝙞𝙨 𝙞𝙨 𝙞𝙩𝙖𝙡𝙞𝙘 𝙩𝙚𝙭𝙩',
    'mono': '𝚃𝚑𝚒𝚜 𝚒𝚜 𝚖𝚘𝚗𝚘 𝚝𝚎𝚡𝚝',
    'small': 'ᵗʰⁱˢ ⁱˢ ˢᵐᵃˡˡ ᵗᵉˣᵗ',
    'wide': 'Ｔｈｉｓ　ｉｓ　ｗｉｄｅ　ｔｅｘｔ'
}

@Client.on_message(filters.command("font", hl) & filters.me)
async def font_gen(client: Client, message: Message):
    if len(message.command) < 3:
        styles = "\n".join([f"• `{hl}font {k} text`" for k in FONT_STYLES.keys()])
        return await edit_or_reply(message, f"**Available Styles:**\n{styles}")
    
    style = message.command[1].lower()
    text = " ".join(message.command[2:])
    
    if style not in FONT_STYLES:
        return await edit_or_reply(message, "Invalid font style!")
    
    # Conversion logic would go here (implementation needed)
    converted = f"`{text}` → {FONT_STYLES[style]}"
    await edit_or_reply(message, converted)
