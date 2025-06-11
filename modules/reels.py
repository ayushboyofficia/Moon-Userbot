import os
import requests
from pyrogram import Client, filters
from pyrogram.types import Message

# Install required package first: pip install instaloader
try:
    import instaloader
except ImportError:
    os.system("pip install instaloader")
    import instaloader

L = instaloader.Instaloader()

@Client.on_message(filters.command("reel") & filters.me)
async def insta_reel_downloader(client: Client, message: Message):
    """Download Instagram Reels by Link"""
    
    if len(message.command) < 2:
        return await message.reply("**Usage:** `.reel <instagram-reel-url>`")

    url = message.command[1]
    
    try:
        # Extract shortcode from URL
        shortcode = url.split("/reel/")[-1].split("/")[0].split("?")[0]
        
        msg = await message.reply("⬇️ Downloading reel...")
        
        # Download reel
        post = instaloader.Post.from_shortcode(L.context, shortcode)
        
        if not post.is_video:
            return await msg.edit("❌ This is not a video reel!")
        
        # Get the best quality video URL
        video_url = post.video_url
        filename = f"reel_{shortcode}.mp4"
        
        # Download video
        with requests.get(video_url, stream=True) as r:
            r.raise_for_status()
            with open(filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        
        # Upload to Telegram
        await msg.edit("⬆️ Uploading...")
        await message.reply_video(
            filename,
            caption=f"🎬 **Instagram Reel**\n\n👤 **By:** [@{post.owner_username}](https://instagram.com/{post.owner_username})"
        )
        
        await msg.delete()
    
    except Exception as e:
        await message.reply(f"❌ Error: `{str(e)}`")
    
    finally:
        if os.path.exists(filename):
            os.remove(filename)

# Help section (if your help system supports it)
try:
    from modules.help import add_command_help
    add_command_help(
        "Instagram",
        [
            ["reel <url>", "Download Instagram reels"],
        ]
    )
except:
    pass
