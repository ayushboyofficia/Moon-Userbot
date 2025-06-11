from PIL import Image, ImageDraw, ImageFont
from pyrogram import Client, filters

@Client.on_message(filters.command("3dtext") & filters.me)
async def three_d_text(client, message):
    text = " ".join(message.command[1:])
    
    # Create 3D text effect
    img = Image.new("RGB", (800, 200), "black")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 80)
    
    # Draw multiple layers for 3D effect
    for i in range(5):
        draw.text((20+i, 50+i), text, font=font, fill="white")
    draw.text((25, 55), text, font=font, fill="red")
    
    img.save("3dtext.jpg")
    await message.reply_photo("3dtext.jpg")
    os.remove("3dtext.jpg")
