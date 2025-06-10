import random
from pyrogram import Client, filters
from config import SUDO_USERS

@Client.on_message(filters.command("loveraid") & (filters.me | filters.user(SUDO_USERS)))
async def love_raid(client, message):
    # Hindi Shayaris with English translations
    shayaris = [
        {
            "hindi": "दिल की बात होंठों पे लाना मुश्किल तो नहीं,\nपर तेरे बिन अब जीना मुमकिन तो नहीं।",
            "english": "Bringing heart's words to lips isn't hard,\nBut living without you is impossible now."
        },
        {
            "hindi": "तुम्हारी यादों का सहारा लेकर,\nहम जिंदगी की राहों पे चल पड़े।",
            "english": "Holding onto memories of you,\nI started walking on life's paths."
        },
        {
            "hindi": "मोहब्बत की राह में मिले थे हम,\nअब हर राह मोहब्बत की लगती है।",
            "english": "We met on the path of love,\nNow every path seems like love."
        },
        # Add 37+ more shayaris in same format
        {
            "hindi": "तेरी यादों के सहारे जी रहे हैं,\nतुम्हारे बिन भी तुम्हारे हैं।",
            "english": "Living on memories of you,\nEven without you, I'm yours."
        }
    ]

    # Select random shayari
    shayari = random.choice(shayaris)
    
    # Format message
    text = f"**❤️ Love Shayari ❤️**\n\n{shayari['hindi']}\n\n_{shayari['english']}_"
    
    # Send to current chat if replied to message
    if message.reply_to_message:
        user = message.reply_to_message.from_user
        text = f"{user.mention}\n\n{text}"
        await message.reply_to_message.reply_text(text)
    else:
        await message.reply_text(text)

from .help import add_command_help
add_command_help(
    "Love",
    [
        ["loveraid", "Send romantic Hindi shayaris with English translations"],
    ]
)
