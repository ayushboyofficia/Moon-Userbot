from pyrogram import Client, filters
import instaloader

L = instaloader.Instaloader()

@Client.on_message(filters.command("reels") & filters.me)
async def download_reels(client, message):
    url = message.command[1]
    post = instaloader.Post.from_shortcode(L.context, url.split("/")[-2])
    await message.reply_video(post.video_url)
