from gggne import gggne
from telethon import events
from os import remove

@gggne.ar_cmd(pattern="(جلب الصورة|ذاتية)")
async def datea(event):
    await event.delete()
    scertpic = await event.get_reply_message()
    downloadlethon = await scertpic.download_media()
    send = await gggne.send_file("me", downloadlethon)
    remove(downloadjmthon)
