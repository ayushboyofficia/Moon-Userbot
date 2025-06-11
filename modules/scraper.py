import os
import requests
import instaloader
from pyrogram import Client, filters
from pyrogram.types import Message
from yt_dlp import YoutubeDL

# Install required packages:
# pip install instaloader yt-dlp requests

L = instaloader.Instaloader()
ydl_opts = {'format': 'best'}

@Client.on_message(filters.command(["scrape", "dl"]) & filters.me)
async def universal_scraper(client: Client, message: Message):
    """Multi-Platform Content Downloader"""
    
    if len(message.command) < 2:
        return await message.reply("**Usage:**\n`.scrape instagram <url>`\n`.scrape youtube <url>`\n`.scrape twitter <url>`")

    platform = message.command[1].lower()
    url = message.command[2] if len(message.command) > 2 else None

    if not url:
        return await message.reply("❗ URL दें!")

    msg = await message.reply(f"🔍 {platform.capitalize()} से डाउनलोड शुरू...")

    try:
        # Instagram Downloader
        if platform == "instagram":
            if "/reel/" in url or "/p/" in url:
                shortcode = url.split("/reel/")[-1].split("/p/")[-1].split("/")[0].split("?")[0]
                post = instaloader.Post.from_shortcode(L.context, shortcode)
                
                if post.is_video:
                    video_url = post.video_url
                    filename = f"insta_{shortcode}.mp4"
                    await download_and_send(video_url, filename, client, message, msg, "video")
                else:
                    await message.reply_photo(post.url, caption=f"📸 Instagram Post\n\n👤 @{post.owner_username}")

            elif "/stories/" in url:
                await message.reply("❗ Stories डाउनलोड करने के लिए Instagram लॉगिन जरूरी है")

        # YouTube Downloader
        elif platform == "youtube":
            with YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                if 'entries' in info:  # Playlist
                    await message.reply("❗ प्लेलिस्ट के लिए `.ytplaylist` कमांड यूज करें")
                else:
                    filename = f"yt_{info['id']}.mp4"
                    await download_and_send(info['url'], filename, client, message, msg, "video")

        # Twitter Downloader
        elif platform == "twitter":
            tweet_id = url.split("/status/")[1].split("?")[0]
            api_url = f"https://twitback.onrender.com/tweet?url={tweet_id}"
            response = requests.get(api_url).json()
            
            if 'video' in response:
                video_url = response['video']
                filename = f"twitter_{tweet_id}.mp4"
                await download_and_send(video_url, filename, client, message, msg, "video")
            else:
                await message.reply("❗ वीडियो नहीं मिला")

    except Exception as e:
        await msg.edit(f"❌ Error: `{str(e)}`")

async def download_and_send(url, filename, client, message, msg, media_type):
    """Helper function to download and send media"""
    try:
        # Download file
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)

        # Send file
        await msg.edit("📤 Uploading...")
        if media_type == "video":
            await message.reply_video(filename)
        elif media_type == "photo":
            await message.reply_photo(filename)

        await msg.delete()
    finally:
        if os.path.exists(filename):
            os.remove(filename)

# Help section
try:
    from modules.help import add_command_help
    add_command_help(
        "Scraper", 
        [
            ["scrape instagram <url>", "Instagram Reels/Posts डाउनलोड करे"],
            ["scrape youtube <url>", "YouTube Videos डाउनलोड करे"],
            ["scrape twitter <url>", "Twitter Videos डाउनलोड करे"],
        ]
    )
except:
    pass
