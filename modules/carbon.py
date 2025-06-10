
import os
import random
import requests
from pyrogram import Client, filters
from pyrogram.types import Message
from config import SUDO_USERS
from .help import *
hl = "."
CARBON_THEMES = [
    "3024-night",
    "a11y-dark",
    "blackboard",
    "base16-dark",
    "base16-light",
    "cobalt",
    "dracula",
    "duotone-dark",
    "hopscotch",
    "lucario",
    "material",
    "monokai",
    "night-owl",
    "nord",
    "oceanic-next",
    "one-light",
    "one-dark",
    "panda-syntax",
    "paraiso-dark",
    "seti",
    "shades-of-purple",
    "solarized-dark",
    "solarized-light",
    "synthwave-84",
    "twilight",
    "verminal",
    "vscode",
    "yeti",
    "zenburn"
]

@Client.on_message(
    filters.command(["carbon", "cr"], hl) & (filters.me | filters.user(SUDO_USERS))
)
async def carbon_func(client: Client, message: Message):
    if not message.reply_to_message:
        return await message.edit("**Please reply to a text message to generate carbon.**")
    
    if not message.reply_to_message.text:
        return await message.edit("**Please reply to a text message to generate carbon.**")
    
    text = message.reply_to_message.text
    m = await message.edit("**Generating Carbon...**")
    
    theme = random.choice(CARBON_THEMES)
    if len(message.command) > 1:
        theme = message.text.split(None, 1)[1].lower()
        if theme not in CARBON_THEMES:
            return await m.edit(f"**Invalid theme! Available themes:**\n`{'`, `'.join(CARBON_THEMES)}`")
    
    carbon_url = f"https://carbonara.solopov.dev/api/cook?code={text}&theme={theme}"
    
    try:
        response = requests.get(carbon_url)
        if response.status_code == 200:
            with open("carbon.png", "wb") as f:
                f.write(response.content)
            await message.reply_photo("carbon.png")
            await m.delete()
            os.remove("carbon.png")
        else:
            await m.edit("**Failed to generate carbon image.**")
    except Exception as e:
        await m.edit(f"**Error:** `{e}`")

add_command_help(
    "•─╼⃝𖠁 Cᴀʀʙᴏɴ",
    [
        ["carbon or .cr", "Generate carbon image from replied text (random theme)"],
        ["carbon <theme> or .cr <theme>", "Generate carbon with specific theme"],
    ],
)
### Features:
1. **Random Theme Selection**: Automatically picks a beautiful theme if none specified
2. **Theme Customization**: Users can specify their preferred theme
3. **Reply-Based**: Works on replied text messages
4. **Error Handling**: Proper error messages for invalid themes or API failures
5. **Cleanup**: Automatically deletes the generated image after sending

### Usage:
1. Reply to a text message with `.carbon` or `.cr`
2. For specific theme: `.carbon dracula` or `.cr material`
3. Available themes are shown if an invalid theme is provided

###
