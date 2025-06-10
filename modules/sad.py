# Moon-Userbot - Sad Pictures Module
# MIT License - Copyright (c) 2024 Moon-Userbot
import random
from pyrogram import Client, filters
from config import SUDO_USERS
from .help import add_command_help
hl = "."
@Client.on_message
    (filters.command(["sad"], hl) & (filters.me | filters.user(SUDO_USERS))
async def send_sad_pic(client, message):
    """Send random sad pictures"""
    sad_pics = [
        "https://graph.org/file/1fbf1067783766f94ffd9.jpg",
        "https://graph.org/file/936d84cb14c8b2fdb7ae6.jpg",
        "https://graph.org/file/32cd9e2af39313214eb07.jpg",
        "https://graph.org/file/05e88df4373abd287b528.jpg",
        "https://graph.org/file/eadd8ce5faabceda933f9.jpg",
        "https://graph.org/file/8f20b6546a0487eecbaed.jpg",
        "https://graph.org/file/9cee901c0fd8c3793eb0e.jpg",
        "https://graph.org/file/44f5282dfd2345a597a1b.jpg",
        "https://graph.org/file/ac1046936f1a681b6c610.jpg",
        "https://graph.org/file/13f5c42aaf324143af205.jpg",
        "https://graph.org/file/7484e4d6b8e8c300be3a7.jpg",
        "https://graph.org/file/166fc6b9878a803763947.jpg",
        "https://graph.org/file/ba4c13bd22b48327c57b1.jpg",
        "https://graph.org/file/edafa7266f9ad3e3fe4e3.jpg",
        "https://graph.org/file/c478e54b027809de8fa5c.jpg",
    ]
    
    try:
        # Delete the command message if sent by me
        if message.from_user.is_self:
            await message.delete()
        
        # Send random sad picture
        pic_url = random.choice(sad_pics)
        await message.reply_photo(pic_url, caption="😢 Here's a sad picture...")
        
    except Exception as e:
        await message.reply(f"Error: {str(e)}")

# Add help text
add_command_help(
    "sad",
    [
        [f"{hl}sad", "Sends a random sad picture"],
    ]
)
