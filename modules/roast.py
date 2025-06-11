import random
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("roast") & filters.me)
async def roast_karo(client: Client, message: Message):
    """70+ Ultimate Roasts - Hindi + English"""
    
    roasts = [
        # Appearance Roasts (20)
        "Tumhare face ko dekh ke camera autofocus band kar deta hai!",
        "Tum jaise logo ke liye Snapchat ne 'No Filter' option banaya hai!",
        "Tumhari shakal dekh ke toh Google Lens bhi crash ho jata hai!",
        "Tumhare baal dekh ke toh Hair Oil companies bhi pareshan hai!",
        "Tumhari smile dekh ke Colgate wale apna ad change kar rahe hai!",
        
        # Intelligence Roasts (15)
        "Tumhara brain toh 2G pe chalta hai - slow aur buffering!",
        "Tumse zyada smart toh mere fridge ka ice-maker hai!",
        "Tumhare liye 'Ctrl+C, Ctrl+V' bhi advanced technology hai!",
        "Tum jaise logon ko dekh ke Albert Einstein bhi apni theory pe doubt karte honge!",
        
        # Personality Roasts (20)
        "Tumhari personality dekh ke introverts bhi party karne lagte hai!",
        "Tumse zyada interesting toh MS Word ka Clippy assistant tha!",
        "Tumhare jokes sun ke toh dad jokes bhi stand-up comedy lagne lage!",
        "Tumhari vibe dekh ke WiFi automatically disconnect ho jata hai!",
        
        # Hindi Special Roasts (15)
        "तुम्हारी फोटो देखकर तो फोटोशॉप भी 'कैंसल' बटन दबा देता है!",
        "तुम्हारे चेहरे को देखकर डार्क मोड भी लाइट मोड में आ जाता है!",
        "तुमसे ज्यादा उपयोगी तो मेरे फोन का चार्जर है - कम से कम वो 100% तक तो चलता है!",
        "तुम्हारी बुद्धिमत्ता देखकर तो कैलकुलेटर भी 'Error' दिखा देता है!",
        
        # Savage Comebacks (10)
        "Tumhare baare mein kuch bolu toh WhatsApp pe 'This message was deleted' aa jayega!",
        "Tum jaise logo ko dekh ke toh 'Do Not Disturb' mode bhi disturb ho jata hai!",
        "Tumhari existence ko justify karne ke liye scientists naye research paper likh rahe hai!",
        "Tumse zyada useful toh 'Close Door' button in elevators hai!",
        
        # Tech Roasts (10)
        "Tumhara processor toh Pentium 1 pe bhi lag karta hoga!",
        "Tumhare liye 'Artificial Intelligence' bhi natural lagta hoga!",
        "Tumhari memory dekh ke RAM bhi expand hone se mana kar deti hai!",
        
        # Food Roasts (5)
        "Tumhare cooking skills dekh ke Maggie bhi '2-minute' se '2-hour' ban gaya!",
        "Tumhari daal itni bland hai ki salt bhi alag se mangti hai!",
        
        # Special 5 Ultra Savage
        "Tumhare life ka brightness level itna low hai ki dark mode bhi reject karta hai!",
        "Tumhari photos upload karte time Instagram 'Low Quality Content' warning deta hai!",
        "Tumhare jokes sunke emojis bhi straight face ban jate hai!",
        "Tumse zyada expressive toh Windows error messages hai!",
        "Tumhari personality dekh ke toh '404 Not Found' bhi sharma jaye!"
    ]
    
    if message.reply_to_message:
        user = message.reply_to_message.from_user
        roast = f"🔥 **ROAST OF THE DAY** 🔥\n\n{user.mention}\n\n{random.choice(roasts)}"
        await message.reply_to_message.reply_text(roast)
    else:
        await message.reply_text("Kisi ko roast karne ke liye uske message pe reply karo! 😏")

    await message.delete()

from .help import add_command_help
add_command_help(
    "Roast",
    [
        ["roast", "Kisi ka jeevan barbaad kar do! (Reply to someone)"],
    ]
)
