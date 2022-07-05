from telethon import events
import random, re
from gggne.utils import admin_cmd
import asyncio 

# Wespr File by  @GGGNE
# Copyright (C) 2021 LETHON TEAM
@borg.on(
    admin_cmd(pattern="همسة ?(.*)")
)
async def wspr(event):
    if event.fwd_from:
        return
    leomr = event.pattern_match.group(1)
    ayah = "@nnbbot"
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    tap = await bot.inline_query(ayah, leomr) 
    await tap[0].click(event.chat_id)
    await event.delete()
    
@borg.on(admin_cmd("م21"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("⌯︙اوامر الهمسه \n\n⌔︙الامر  • `.همسة`\n⌔︙الاستخدام  • لكتابة همسه سرية لشخص في المجموعه \n\n⌯︙الامر • `.الهمسة`\n⌯︙استخدامه • لعرض كيفية كتابة همسة سرية\n\n⌯︙CH  - @GGGNE")
        
@borg.on(admin_cmd("الهمسة"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("**⌯︙شـرح كيـفية كـتابة همـسة سـرية**\n⌯︙اولا اكتب الامر  .همسة  بعدها الرسالة بعدها اكتب معرف الشخص\n⌯︙مـثال  :   `.همسة ههلا @GGGNE`")