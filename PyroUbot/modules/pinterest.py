import requests
import wget
import os
import random
from pyrogram import Client
from PyroUbot import *

__MODULE__ = "pinterest"
__HELP__ = """
<blockquote><b>『 pinterest 』</b>

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}pinsearch</code> 
   <i>penjelasan:</b> mendowload media dari pencarian</i></blockquote>
"""

@PY.UBOT("pinsearch")
async def pin(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    
    jalan = await message.reply(f"{prs} Processing...")
    
    if len(message.command) != 2:
        return await jalan.edit(f"{ggl} Example .pinsearch asuna")
    
    link = message.command[1]
    a = message.text.split(' ', 1)[1]
    chat_id = message.chat.id
    url = f"https://widipe.com/pinterest?query={a}"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            hasil = data['result']
            random_result = random.choice(hasil)
            caption = f"""
<emoji id=5841235769728962577>⭐</emoji>PinUrl: 
<emoji id=5843952899184398024>⭐</emoji>Title: 
"""
            photo_path = wget.download(random_result)
            await client.send_photo(chat_id, caption=caption, photo=photo_path)
            if os.path.exists(photo_path):
                os.remove(photo_path)
            
            await jalan.delete()
        else:
            await jalan.edit(f"{ggl} No 'result' key found in the response.")
    
    except requests.exceptions.RequestException as e:
        await jalan.edit(f"{ggl} Request failed: {e}")
    
    except Exception as e:
        await jalan.edit(f"{ggl} An error occurred: {e}")
