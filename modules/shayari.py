from Moon import *
from Moon import MoonBot
from Moon.helpers import *

shayari_list = [
    "दिल तोड़ने वालों को मिलते रहेंगे सज्जन,\nहम जैसे ही किसी के हो जाएंगे, खुदा का शुक्र अदा करेंगे।",
    "मोहब्बत की राह में चलना सीख लो,\nजिंदगी भर के लिए याद आऊंगा मैं तुम्हें।",
    "तुम्हारी याद के सिवा कुछ भी नहीं,\nतुम्हारे बिना जिंदगी अधूरी सी लगती है।",
    # यहाँ और शायरियाँ जोड़ें
    "ख्वाबों में भी तुम आओ तो डर लगता है,\nवरना हम तो तन्हाई में भी साथ रहते हैं।"
]

@MoonBot.on(events.NewMessage(pattern="^[.!/]shayari$"))
async def shayari(event):
    try:
        random_shayari = random.choice(shayari_list)
        await event.reply(random_shayari)
    except Exception as e:
        await event.reply(f"Error: {str(e)}")

@MoonBot.on(events.NewMessage(pattern="^[.!/]shayari (.*)"))
async def add_shayari(event):
    if event.sender_id not in SUDO_USERS:
        return await event.reply("⚠️ यह सिर्फ Sudo Users के लिए है!")
    
    new_shayari = event.pattern_match.group(1)
    if len(new_shayari) < 10:
        return await event.reply("❌ Shayari बहुत छोटी है!")
    
    shayari_list.append(new_shayari)
    await event.reply("✅ नई Shayari सफलतापूर्वक जोड़ दी गई है!")
