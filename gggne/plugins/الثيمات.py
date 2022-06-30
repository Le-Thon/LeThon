import os
import random

from PIL import Image, ImageDraw, ImageFont
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import InputMessagesFilterDocument, InputMessagesFilterPhotos

from gggne import gggne

from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.utils import reply_id
from . import gggne, mention

@gggne.on(admin_cmd(outgoing=True, pattern="ثيم$"))
async def LeThe(theme):
  rl = random.randint(2,510)
  url = f"https://t.me/IUUZZ/{rl}"
  await theme.client.send_file(theme.chat_id,url,caption="⌯︙THEME BY : @GGGNE 🎊",parse_mode="html")
  await theme.delete()