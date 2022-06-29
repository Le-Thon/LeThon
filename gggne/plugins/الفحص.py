import random
import time
from datetime import datetime
from platform import python_version

from telethon import version
from telethon.errors.rpcerrorlist import (
    MediaEmptyError,
    WebpageCurlFailedError,
    WebpageMediaEmptyError,
)

from gggne import StartTime, gggne, gggneversion

from ..core.managers import edit_or_reply
from ..helpers.functions import check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus
from . import mention


@gggne.ar_cmd(pattern="فحص$")
async def amireallyalive(event):
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    gggneevent = await edit_or_reply(
        event,
        "**⌔∮ عزيزي المستخدم اذا هذه الرسالة بقت ولم تظهر لك كليشه الفحص يرجى اضاف الكليشه بشكل صحيح مره اخرى**",
    )
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    _, check_sgnirts = check_data_base_heal_th()
    EMOJI = gvarstatus("ALIVE_EMOJI") or "  ✥ "
    ALIVE_TEXT = gvarstatus("ALIVE_TEXT") or "₰ [LeThon arabic userbot](t.me/gggne) ₰"
    gggne_IMG = gvarstatus("ALIVE_PIC")
    gggne_caption = gvarstatus("ALIVE_TEMPLATE") or temp
    caption = gggne_caption.format(
        ALIVE_TEXT=ALIVE_TEXT,
        EMOJI=EMOJI,
        mention=mention,
        uptime=uptime,
        telever=version.__version__,
        jmver=gggneversion,
        pyver=python_version(),
        dbhealth=check_sgnirts,
        ping=ms,
    )
    if gggne_IMG:
        gggne = [x for x in gggne_IMG.split()]
        PIC = random.choice(gggne)
        try:
            await event.client.send_file(
                event.chat_id, PIC, caption=caption, reply_to=reply_to_id
            )
            await gggneevent.delete()
        except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
            return await edit_or_reply(
                gggneevent,
                f"**⌔∮ عليك استخدام رابط تليجراف لا يمكن استخدام اي رابط ثاني واعد استخدام الامر  ⪼  `.اضف صورة الحماية` <بالرد على الرابط> ",
            )
    else:
        await edit_or_reply(
            gggneevent,
            caption,
        )


temp = """{ALIVE_TEXT}
**{EMOJI} قاعدۿ البيانات :** `{dbhealth}`
**{EMOJI} أصـدار التـيليثون :** `{telever}`
**{EMOJI} أصـدار ليـثون :** `{jmver}`
**{EMOJI} الوقت:** `{uptime}` 
**{EMOJI} أصدار البـايثون :** `{pyver}`
**{EMOJI} المسـتخدم:** {mention}"""



from gggne import gggne
from telethon import events
from telethon import version
from platform import python_version

@gggne.ar_cmd(pattern="ليثون$")
async def _(event):
    await event.delete()
    iiizfget = await event.get_sender()
    hnarsl = event.to_id
    iiizf_pic = "https://telegra.ph/file/7bac18f40e26d091b6720.jpg"
    await gggne.send_file(hnarsl, iiizf_pic, caption=f"اهلا بك {iiizfget.first_name}\n\n اصدار ليثون: 5.0.0\n اصدار البايثون: {python_version()}\n اصدار التيليثون: {version.__version__}\n\nشكرا لك\nليثون™")
