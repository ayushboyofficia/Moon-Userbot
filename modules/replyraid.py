from pyrogram import Client, filters
import random
import asyncio

# Raid Target
TARGET_USER = None

# 300+ Ultimate Creative Galis (Hindi + English)
GALI_DB = [
    # Funny/Sarcastic (50)
    "Tere jaise ko dekh ke toh Google bhi 'No results found' dikhata hai!",
    "Teri shakal dekh ke toh camera autofocus band kar deta hai!",
    "Tere baap ne teri photo dekh ke hi phone change kar liya hoga!",
    "Tere jaisa chutiya maine sirf TV serials mein dekha hai!",
    "Tere dimaag ka processor toh Pentium 1 bhi nahi hai!",
    
    # Rhyming Gaalis (50)
    "Teri maa ki chut, teri behen ki gaand, dono ko mila ke bana dunga sandwich!",
    "Chal hatt behen ke lode, warna teri gaand mein daal dunga rode!",
    "Teri maa ka bhosda, teri behen ki chut, dono ko chod ke bana dunga halwa!",
    
    # English Creative (50)
    "Your face looks like it was on fire and someone tried to put it out with a fork!",
    "If I wanted to kill myself, I'd climb your ego and jump to your IQ!",
    "You're so ugly, when you were born, the doctor slapped your mother!",
    
    # Bollywood Style (50)
    "Tere jaise chutiye ko dekh ke toh Gabbar Singh bhi shock ho jaye!",
    "Mogambo khush hua... ki usse tere jaisa chutiya kabhi nahi mila!",
    "Kitne aadmi the? Ek teri maa, ek teri behen, aur main... triple role mein!",
    
    # Gaon Wali Gaali (50)
    "Teri maa ko gaon ke kutton ne choda hai!",
    "Teri behen ki shaadi mein DJ ne bhi teri maa ko chod diya!",
    "Teri maa ki chut mein bheed hai, line se lag ke chodo!",
    
    # Tech Gaali (50)
    "Tere dimaag ka RAM itna kam hai ki Chrome bhi nahi chalta!",
    "Tere jaise chutiye ko dekh ke Alexa bhi mute ho jati hai!",
    "Tere face ka resolution itna low hai ki 144p pe bhi blur dikhta hai!"
]

@Client.on_message(filters.command("replyraid") & filters.me)  
async def start_reply_raid(client, message):  
    global TARGET_USER  

    if not message.reply_to_message:  
        return await message.reply("**Usage:** `.replyraid` (Reply to user)")  

    TARGET_USER = message.reply_to_message.from_user.id  
    await message.edit(f"**💥 REPLY RAID STARTED ON USER!**")  

@Client.on_message(filters.incoming)  
async def auto_reply_raid(client, message):  
    global TARGET_USER  

    if TARGET_USER and message.from_user.id == TARGET_USER:  
        for _ in range(3):  # 3 replies per message
            gali = random.choice(GALI_DB)
            await message.reply(gali)
            await asyncio.sleep(0.5)  

@Client.on_message(filters.command("stopraid") & filters.me)  
async def stop_reply_raid(client, message):  
    global TARGET_USER  
    TARGET_USER = None  
    await message.edit("**🛑 REPLY RAID STOPPED!**")
