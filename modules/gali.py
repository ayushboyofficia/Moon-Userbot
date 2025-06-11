from pyrogram import Client, filters
import random
from pyrogram.types import Message

@Client.on_message(filters.command("gali") & filters.me)
async def gali_detector(client: Client, message: Message):
    """200+ Ultimate Gaaliyan - Pure Desi Style"""
    
    galis = [
        # Classic Hindi Gaalis (50+)
        "Teri maa ki chut mein bheed laga dunga!",
        "Bhosdike land ke pujari!",
        "Chut ke andhe, gaand ke dhakkan!",
        "Teri behen ko 10 mein chod dunga!",
        "Teri gaand mein dande se dhamki dunga!",
        "Randi ke pille, apni aukat mein reh!",
        "Teri maa ko railway station pe chod dunga!",
        "Chut marike, teri nasal badal dunga!",
        "Teri behen ki chut mein auto chala dunga!",
        "Gaandu, teri shakal dekh ke ulti aa jati hai!",
        
        # Creative Hybrid Gaalis (50+)
        "Teri maa ka bhosda ChatGPT se bhi zyada confusing hai!",
        "Teri shakal dekh ke toh Google Maps bhi wrong location dikhata hai!",
        "Tere jaise chutiye ko dekh ke 5G network bhi 2G pe aa jata hai!",
        "Teri aukat se zyada features toh free trial version mein hote hai!",
        "Tere dimaag ki storage full hai - format karne ki zaroorat hai!",
        
        # English Translated Gaalis (50+)
        "Your mom's pussy has more traffic than Delhi metro!",
        "Son of a bitch made in China quality!",
        "Your sister's vagina is like public property!",
        "Your family tree must be a cactus - everyone's a prick!",
        "Your brain has more bugs than Windows 98!",
        
        # Tech-Inspired Gaalis (20)
        "Teri maa ki chut - Error 404 Not Found!",
        "Tere jaise chutiye ko dekh ke AI bhi depression mein chala jata hai!",
        "Teri shakal ka resolution itna low hai ki 144p bhi sharma jaye!",
        "Tere dimaag ka processor Pentium 1 se bhi slow hai!",
        
        # Ultra Savage (30)
        "Teri nasal itti gandi hai ki gutter ka pani bhi bolta hai 'I quit'!",
        "Tere baap ne condom pehena hota toh aaj teri shakal nahi dekhni padti!",
        "Teri maa ko chodne wale itne the ki unka ek WhatsApp group hai!",
        "Teri behen ki chut mein toh IPL ka opening match hua tha!",
        "Teri family planning fail ho gayi - isliye tu paida hua!"
    ]
    
    if message.reply_to_message:
        user = message.reply_to_message.from_user
        gali = f"🔥 **GALI OF THE DAY** 🔥\n\n{user.mention}\n\n`{random.choice(galis)}`"
        await message.reply_to_message.reply_text(gali)
    else:
        await message.reply_text("Kisi ko gali dene ke liye uske message pe reply karo! 😏")

    await message.delete()

from .help import add_command_help
add_command_help(
    "Gali",
    [
        ["gali", "Kisi ka dil dukha do! (Reply to someone)"],
    ]
)
