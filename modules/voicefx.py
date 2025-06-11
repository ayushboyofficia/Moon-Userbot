import os
import random
import numpy as np
import soundfile as sf
from pyrogram import Client, filters
from pyrogram.types import Message

# Install required packages: 
# pip install numpy soundfile

@Client.on_message(filters.command("voicefx") & filters.me)
async def voice_effects(client: Client, message: Message):
    """किसी वॉइस मैसेज को अलग-अलग इफेक्ट्स दें!"""
    
    if not message.reply_to_message or not message.reply_to_message.voice:
        return await message.reply("❗ किसी वॉइस मैसेज को रिप्लाई करें!")

    try:
        # Download voice message
        voice_msg = await message.reply_to_message.download("voice.ogg")
        
        # Apply effects
        data, samplerate = sf.read(voice_msg)
        
        # Random effect selection
        effect_type = random.choice(["high_pitch", "low_pitch", "robot", "alien"])
        
        if effect_type == "high_pitch":
            new_data = data * 1.5  # High pitch
        elif effect_type == "low_pitch":
            new_data = data * 0.5  # Low pitch
        elif effect_type == "robot":
            new_data = np.sin(data)  # Robot voice
        else:
            new_data = data + np.random.normal(0, 0.1, len(data))  # Alien voice
        
        # Save and send
        sf.write("modified_voice.ogg", new_data, samplerate)
        await message.reply_voice("modified_voice.ogg")
        
    except Exception as e:
        await message.reply(f"❌ Error: `{str(e)}`")
    
    finally:
        # Cleanup
        if os.path.exists("voice.ogg"):
            os.remove("voice.ogg")
        if os.path.exists("modified_voice.ogg"):
            os.remove("modified_voice.ogg")

# Help Menu (if available)
try:
    from modules.help import add_command_help
    add_command_help(
        "VoiceFX",
        [
            ["voicefx", "वॉइस मैसेज को फनी इफेक्ट्स दें (रिप्लाई करके)"],
        ]
    )
except:
    pass
