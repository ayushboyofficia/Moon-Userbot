import numpy as np
import soundfile as sf
from pyrogram import Client, filters

@Client.on_message(filters.command("voicefx") & filters.me)
async def voice_effects(client, message):
    if not message.reply_to_message or not message.reply_to_message.voice:
        return await message.reply("किसी वॉइस मैसेज को रिप्लाई करो!")

    voice = await message.reply_to_message.download("voice.ogg")
    
    # Apply voice effects
    data, samplerate = sf.read(voice)
    
    # Random effect selection
    effect = random.choice([
        lambda x: x * 1.5,  # High pitch
        lambda x: x * 0.5,  # Low pitch
        lambda x: np.sin(x), # Robot voice
        lambda x: x + np.random.normal(0, 0.1, len(x))  # Alien voice
    ])
    
    new_voice = effect(data)
    sf.write("effect.ogg", new_voice, samplerate)
    
    await message.reply_voice("effect.ogg")
    os.remove(voice)
    os.remove("effect.ogg")
