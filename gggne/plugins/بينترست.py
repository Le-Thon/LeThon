import re

from Leo.strings import get_download_url
from gggne import gggne


@gggne.ar_cmd(pattern="بينترست?(.*)")
async def _(event):
    R = event.pattern_match.group(1)
    links = re.findall(r"\bhttps?://.*\.\S+", R)
    await event.delete()
    if not links:
        Z = await event.respond("▾∮ يجب عليك وضع رابط لتحميله")
        await asyncio.sleep(2)
        await Z.delete()
    else:
        pass
    A = await event.respond("▾∮ يتم التحميل انتظر قليلا")
    GGGNE = get_download_url(R)
    await event.client.send_file(event.chat.id, GGGNE)
    await A.delete()
