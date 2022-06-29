from telethon import Button, events
import re
from telethon.events import CallbackQuery
from gggne import gggne
from ..core import check_owner
from . import *
from ..Config import Config

ROZ_PIC = "https://telegra.ph/file/5f6ef13851dcf0d6fc72b.jpg"
LEO = Config.TG_BOT_USERNAME
ROZ_T = (
    f"**⌯︙بوت جمثـون يعمل بنجاح 🤍،**\n"
    f"**   - اصدار التليثون :** `1.23.0\n`"
    f"**   - اصدار ليثون :** `4.0.0`\n"
    f"**   - البوت المستخدم :** `{LEO}`\n"
    f"**   - اصدار البايثون :** `3.9.6\n`"
    f"**   - المستخدم :** {mention}\n"
)

if Config.TG_BOT_USERNAME is not None and tgbot is not None:

    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        await bot.get_me()
        if query.startswith("السورس") and event.query.user_id == bot.uid:
            buttons = [
                [
                    Button.url("قنـاة السـورس ⚙️", "https://t.me/GGGNE"),
                    Button.url("المطـور 👨🏼‍💻", "https://t.me/GGGNE"),
                ]
            ]
            if ROZ_PIC and ROZ_PIC.endswith((".jpg", ".png", "gif", "mp4")):
                result = builder.photo(
                    ROZ_PIC, text=ROZ_T, buttons=buttons, link_preview=False
                )
            elif ROZ_PIC:
                result = builder.document(
                    ROZ_PIC,
                    title="gggne - gggne",
                    text=ROZ_T,
                    buttons=buttons,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    title="gggne - gggne",
                    text=ROZ_T,
                    buttons=buttons,
                    link_preview=False,
                )
            await event.answer([result] if result else None)


@gggne.ar_cmd(pattern="السورس")
async def repo(event):
    IIIZF = Config.TG_BOT_USERNAME
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await bot.inline_query(IIIZF, "السورس")
    await response[0].click(event.chat_id)
    await event.delete()


# edit by ~ @GGGNE
