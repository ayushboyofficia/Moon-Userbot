import instaloader
import praw
import tweepy
from pyrogram import Client, filters

# API Keys
INSTA_USER = "your_username"
INSTA_PASS = "your_password"
REDDIT_ID = "your_reddit_id"
REDDIT_SECRET = "your_reddit_secret"
TWITTER_KEY = "your_twitter_key"

@Client.on_message(filters.command("scrape") & filters.me)
async def social_scraper(client, message):
    if len(message.command) < 3:
        return await message.reply("Usage: `.scrape <platform> <username>`")

    platform = message.command[1].lower()
    username = message.command[2]
    msg = await message.reply(f"🔍 Scraping {username} from {platform}...")

    try:
        if platform == "instagram":
            L = instaloader.Instaloader()
            L.login(INSTA_USER, INSTA_PASS)
            profile = instaloader.Profile.from_username(L.context, username)
            await message.reply_photo(profile.get_profile_pic_url())
        
        elif platform == "reddit":
            reddit = praw.Reddit(
                client_id=REDDIT_ID,
                client_secret=REDDIT_SECRET,
                user_agent="my user agent"
            )
            for submission in reddit.redditor(username).submissions.new(limit=5):
                await message.reply(submission.url)
        
        elif platform == "twitter":
            auth = tweepy.OAuthHandler(TWITTER_KEY, "")
            api = tweepy.API(auth)
            tweets = api.user_timeline(screen_name=username, count=5)
            for tweet in tweets:
                await message.reply(tweet.text)
        
        await msg.edit("✅ Scraping Complete!")
    except Exception as e:
        await msg.edit(f"❌ Error: {e}")

# Help Menu
from .help import add_command_help
add_command_help(
    "Scraper",
    [
        ["scrape instagram <username>", "Instagram Profile pic"],
        ["scrape reddit <username>", "Reddit post"],
        ["scrape twitter <username>", "Twitter post"],
    ]
)
