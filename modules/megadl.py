import os
import asyncio
import yt_dlp
import libtorrent as lt
from pyrogram import Client, filters
from mega import Mega

mega = Mega()

@Client.on_message(filters.command("megadl") & filters.me)
async def mega_downloader(client, message):
    if len(message.command) < 2:
        return await message.reply("Usage: `.megadl <url>`")

    url = message.command[1]
    msg = await message.reply("🔍 Analyzing Link...")

    # YouTube Download
    if "youtube.com" in url or "youtu.be" in url:
        ydl_opts = {
            'format': 'best',
            'outtmpl': 'downloads/%(title)s.%(ext)s',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            await msg.edit("📤 Uploading...")
            await message.reply_video(f"downloads/{info['title']}.mp4")
    
    # Torrent Download
    elif url.startswith("magnet:"):
        ses = lt.session()
        h = lt.add_magnet_uri(ses, url)
        await msg.edit("🧲 Torrent Download Started!")
    
    # MEGA.nz Download
    elif "mega.nz" in url:
        m = mega.login()
        file = m.download_url(url)
        await msg.edit("📁 MEGA File Downloaded!")
    
    else:
        await msg.edit("⚠️ Unsupported Link!")

    os.remove("downloads/*")  # Cleanup

# Help Menu
from .help import add_command_help
add_command_help(
    "Downloader",
    [
        ["megadl <url>", "YouTube/Torrent/MEGA सब कुछ डाउनलोड करेगा!"],
    ]
)
