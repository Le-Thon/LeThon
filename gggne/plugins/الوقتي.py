# اذا تخمط اذكر الحقوق رجاءا  -
# كتابة وتعديل وترتيب  ~ @GGGNE
# For ~ @gggne

import asyncio
import base64
import os
import shutil
import time
from datetime import datetime

from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.errors import FloodWaitError
from telethon.tl import functions

from ..Config import Config
from ..helpers.utils import _format
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from . import edit_delete, gggne, logging

DEFAULTUSERBIO = Config.DEFAULT_BIO or " ﴿ لا تَحزَن إِنَّ اللَّهَ مَعَنا ﴾  "
DEFAULTUSER = Config.AUTONAME or Config.ALIVE_NAME
LOGS = logging.getLogger(__name__)
CHANGE_TIME = int(gvarstatus("CHANGE_TIME")) if gvarstatus("CHANGE_TIME") else 60


FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"

autopic_path = os.path.join(os.getcwd(), "gggne", "original_pic.png")
digitalpic_path = os.path.join(os.getcwd(), "gggne", "digital_pic.png")
autophoto_path = os.path.join(os.getcwd(), "gggne", "photo_pfp.png")

digitalpfp = Config.DIGITAL_PIC or "https://telegra.ph/file/63a826d5e5f0003e006a0.jpg"
IIIZF = Config.TIME_JM or ""

normzltext = "1234567890"
namerzfont = Config.TI_FN or "𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫𝟢"


async def digitalpicloop():
    DIGITALPICSTART = gvarstatus("digitalpic") == "true"
    i = 0
    while DIGITALPICSTART:
        if not os.path.exists(digitalpic_path):
            downloader = SmartDL(digitalpfp, digitalpic_path, progress_bar=False)
            downloader.start(blocking=False)
            while not downloader.isFinished():
                pass
        shutil.copy(digitalpic_path, autophoto_path)
        Image.open(autophoto_path)
        current_time = datetime.now().strftime("%I:%M")
        img = Image.open(autophoto_path)
        drawn_text = ImageDraw.Draw(img)
        roz = str(base64.b64decode("dXNlcmJvdC9oZWxwZXJzL3N0eWxlcy9QYXliQWNrLnR0Zg=="))[
            2:36
        ]
        fnt = ImageFont.truetype(roz, 65)
        drawn_text.text((300, 400), current_time, font=fnt, fill=(280, 280, 280))
        img.save(autophoto_path)
        file = await gggne.upload_file(autophoto_path)
        try:
            if i > 0:
                await gggne(
                    functions.photos.DeletePhotosRequest(
                        await gggne.get_profile_photos("me", limit=1)
                    )
                )
            i += 1
            await gggne(functions.photos.UploadProfilePhotoRequest(file))
            os.remove(autophoto_path)
            await asyncio.sleep(60)
        except BaseException:
            return
        DIGITALPICSTART = gvarstatus("digitalpic") == "true"


async def autoname_loop():
    AUTONAMESTART = gvarstatus("autoname") == "true"
    while AUTONAMESTART:
        time.strftime("%d-%m-%y")
        HM = time.strftime("%I:%M")
        for normal in HM:
            if normal in normzltext:
                namefont = namerzfont[normzltext.index(normal)]
                HM = HM.replace(normal, namefont)
        name = f"{IIIZF} {HM}"
        LOGS.info(name)
        try:
            await gggne(functions.account.UpdateProfileRequest(first_name=name))
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(CHANGE_TIME)
        AUTONAMESTART = gvarstatus("autoname") == "true"


async def autobio_loop():
    AUTOBIOSTART = gvarstatus("autobio") == "true"
    while AUTOBIOSTART:
        time.strftime("%d.%m.%Y")
        HI = time.strftime("%I:%M")
        for normal in HI:
            if normal in normzltext:
                namefont = namerzfont[normzltext.index(normal)]
                HI = HI.replace(normal, namefont)
        bio = f"{DEFAULTUSERBIO} {HI}"
        LOGS.info(bio)
        try:
            await gggne(functions.account.UpdateProfileRequest(about=bio))
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(CHANGE_TIME)
        AUTOBIOSTART = gvarstatus("autobio") == "true"


@gggne.ar_cmd(pattern="الصورة الوقتية$")
async def _(event):
    downloader = SmartDL(digitalpfp, digitalpic_path, progress_bar=False)
    downloader.start(blocking=False)
    while not downloader.isFinished():
        pass
    if gvarstatus("digitalpic") is not None and gvarstatus("digitalpic") == "true":
        return await edit_delete(event, "**⌔∮ الصورة الوقتية شغالة بالأصل**")
    addgvar("digitalpic", True)
    await edit_delete(event, "**⌔∮ تم تفعيل الصورة الوقتية بنجاح **")
    await digitalpicloop()


@gggne.ar_cmd(pattern="اسم وقتي$")
async def _(event):
    if gvarstatus("autoname") is not None and gvarstatus("autoname") == "true":
        return await edit_delete(event, "**الاسم الوقتي شغال بالأصل **")
    addgvar("autoname", True)
    await edit_delete(event, "**تم تفعيل الاسم الوقتي بنجاح ✅**")
    await autoname_loop()


@gggne.ar_cmd(pattern="بايو وقتي$")
async def _(event):
    if gvarstatus("autobio") is not None and gvarstatus("autobio") == "true":
        return await edit_delete(event, "**⪼ البايو الوقتي شغال بالأصل**")
    addgvar("autobio", True)
    await edit_delete(event, "**⌔∮ تم تفعيل البايو الوقتي بنجاح**")
    await autobio_loop()


@gggne.ar_cmd(pattern="انهاء ([\s\S]*)")
async def _(event):
    input_str = event.pattern_match.group(1)
    if (
        input_str == "الصورة الوقتية"
        or input_str == "الصورة الوقتيه"
        or input_str == "الصوره الوقتيه"
        or input_str == "صورة وقتية"
        or input_str == "صورة وقتيه"
        or input_str == "صوره وقتية"
    ):
        if gvarstatus("digitalpic") is not None and gvarstatus("digitalpic") == "true":
            delgvar("digitalpic")
            await event.client(
                functions.photos.DeletePhotosRequest(
                    await event.client.get_profile_photos("me", limit=1)
                )
            )
            return await edit_delete(event, "**⌔∮ تم ايقاف الصورة الوقتية بنجاح**")
        return await edit_delete(event, "**⌔∮ لم يتم تفعيل الصورة الوقتية بالأصل**")
    if (
        input_str == "اسم وقتي"
        or input_str == "اسم الوقتي"
        or input_str == "الاسم الوقتي"
        or input_str == "الاسم وقتي"
    ):
        if gvarstatus("autoname") is not None and gvarstatus("autoname") == "true":
            delgvar("autoname")
            await event.client(
                functions.account.UpdateProfileRequest(first_name=DEFAULTUSER)
            )
            return await edit_delete(event, "**⌔∮ تم ايقاف  الاسم الوقتي بنجاح **")
        return await edit_delete(event, "**⌔∮ لم يتم تفعيل الاسم الوقتي بالأصل**")
    if input_str == "بايو وقتي" or input_str == "البايو الوقتي":
        if gvarstatus("autobio") is not None and gvarstatus("autobio") == "true":
            delgvar("autobio")
            await event.client(
                functions.account.UpdateProfileRequest(about=DEFAULTUSERBIO)
            )
            return await edit_delete(event, "**⪼ تم ايقاف البايو الوقتي بنجاح 𓆰**")
        return await edit_delete(event, "**⌔∮ لم يتم تفعيل البايو الوقتي**")
    END_CMDS = [
        "الصورة الوقتية",
        "الصورة الوقتيه",
        "الصوره الوقتيه",
        "الصوره الوقتية",
        "صورة وقتية",
        "صوره وقتيه",
        "اسم وقتي",
        "اسم وقتي",
        "اسم الوقتي",
        "الاسم وقتي",
        "الاسم الوقتي",
        "بايو وقتي",
        "البايو الوقتي",
    ]
    if input_str not in END_CMDS:
        await edit_delete(
            event,
            f"⌔∮ عذرا يجب استخدام الامر بشكل صحيح",
            parse_mode=_format.parse_pre,
        )


gggne.loop.create_task(digitalpicloop())
gggne.loop.create_task(autoname_loop())
gggne.loop.create_task(autobio_loop())
