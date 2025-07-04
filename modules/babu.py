import random
from pyrogram import Client, filters

@Client.on_message(filters.command("babu") & filters.me)
async def babu_command(client, message):
    babu_images = [
        "https://graph.org/file/927054b1716328923e8a8.jpg",
        "https://graph.org/file/1ec2fa6d370139f8b21ff.jpg",
        "https://graph.org/file/8217e49625899dd4df394.jpg",
        "https://graph.org/file/7f37059942a0c1f0d1801.jpg",
        "https://graph.org/file/da4fd4efe47707923f5a6.jpg",
        "https://graph.org/file/df868cea1fb8509eb000b.jpg",
        "https://graph.org/file/0fce98e1919f0f3a1918c.jpg",
        "https://graph.org/file/ad482c3533641a144e488.jpg",
        "https://graph.org/file/b1980a9483a5566fb2a3a.jpg",
        "https://graph.org/file/e2fa8825eec92bdab2c75.jpg",
        "https://graph.org/file/bb2c0476faf73e8e8ccca.jpg",
        "https://graph.org/file/b26ad260e861b2283916f.jpg",
        "https://graph.org/file/081a8de0142b18093d227.jpg",
        "https://graph.org/file/45a0111a6f2a8ac64e7cd.jpg",
        "https://graph.org/file/13cfd2068b0d047d0c496.jpg",
        "https://graph.org/file/d4bc0d3e3ce50f923fe48.jpg",
        "https://graph.org/file/bc0d042034e26fa376197.jpg",
        "https://graph.org/file/169cd16546d8601923d31.jpg",
        "https://graph.org/file/5dc39a92aa30df61226e2.jpg",
        "https://graph.org/file/70a34e9aa6f3cd58948a7.jpg",
        "https://graph.org/file/6becf8b138944221b9bf3.jpg",
        "https://graph.org/file/5a86b96f5a79a6c14b473.jpg",
        "https://graph.org/file/bad0c9945288ed6fc4767.jpg",
        "https://graph.org/file/a0cb4a2508feb2507a727.jpg",
        "https://graph.org/file/0f01c66c6ce27b0571ecd.jpg",
        "https://graph.org/file/bbbe3a3aabc40db36d525.jpg",
        "https://graph.org/file/e938846bf28896eb7c32a.jpg",
        "https://graph.org/file/f0c1318add77bc53e5d86.jpg",
        "https://graph.org/file/98221f45cf0710b72d605.jpg",
        "https://graph.org/file/99c363b9074ca85825909.jpg",
        "https://graph.org/file/a63bd97470fea4fb4a2ed.jpg",
        "https://graph.org/file/949a4c5c6f7f816ffe053.jpg",
        "https://graph.org/file/64aaba8481cfcc8c026ef.jpg",
        "https://graph.org/file/cf2debcc5cd55c09bdd29.jpg",
        "https://graph.org/file/792c1520c6e0896097a58.jpg",
        "https://graph.org/file/c07ada980d32643375197.jpg",
        "https://graph.org/file/1c1d1e2965c549b83422f.jpg",
        "https://graph.org/file/2d52f3557403f22b4f89b.jpg",
        "https://graph.org/file/d3564a34d33fc3c662c65.jpg",
        "https://graph.org/file/71d41d21f9b43ca7217a8.jpg",
        "https://graph.org/file/167410f1fec5dd13d5efc.jpg",
        "https://graph.org/file/639db6810d53820426b5d.jpg",
        "https://graph.org/file/b9a8ec68b3a0710742823.jpg"
    ]
    
    try:
        await message.reply_photo(random.choice(babu_images))
    except Exception as e:
        await message.reply(f"Error: {e}")

# अगर help सिस्टम काम नहीं कर रहा है तो इससे बचने का तरीका
try:
    from modules.help import add_command_help
    add_command_help(
        "Babu",
        [
            ["babu", "रैंडम Babu तस्वीरें भेजता है"],
        ]
    )
except ImportError:
    print("Help system not available, skipping help text addition")
