import os
from typing import Optional

from moviepy.editor import VideoFileClip
from PIL import Image

from ...core.logger import logging
from ...core.managers import edit_or_reply
from ..tools import media_type
from .utils import runcmd

LOGS = logging.getLogger(__name__)


async def media_to_pic(event, reply, noedits=False):  # sourcery no-metrics
    mediatype = media_type(reply)
    if mediatype not in [
        "Photo",
        "Round Video",
        "Gif",
        "Sticker",
        "Video",
        "Voice",
        "Audio",
        "Document",
    ]:
        return event, None
    if not noedits:
        gggneevent = await edit_or_reply(
            event, "**⎙ :: جاري التحويل انتظر قليلا  ** ...."
        )

    else:
        gggneevent = event
    gggnemedia = None
    gggnefile = os.path.join("./temp/", "meme.png")
    if os.path.exists(gggnefile):
        os.remove(gggnefile)
    if mediatype == "Photo":
        gggnemedia = await reply.download_media(file="./temp")
        im = Image.open(gggnemedia)
        im.save(gggnefile)
    elif mediatype in ["Audio", "Voice"]:
        await event.client.download_media(reply, gggnefile, thumb=-1)
    elif mediatype == "Sticker":
        gggnemedia = await reply.download_media(file="./temp")
        if gggnemedia.endswith(".tgs"):
            gggnecmd = f"lottie_convert.py --frame 0 -if lottie -of png '{gggnemedia}' '{gggnefile}'"
            stdout, stderr = (await runcmd(gggnecmd))[:2]
            if stderr:
                LOGS.info(stdout + stderr)
        elif gggnemedia.endswith(".webp"):
            im = Image.open(gggnemedia)
            im.save(gggnefile)
    elif mediatype in ["Round Video", "Video", "Gif"]:
        await event.client.download_media(reply, gggnefile, thumb=-1)
        if not os.path.exists(gggnefile):
            gggnemedia = await reply.download_media(file="./temp")
            clip = VideoFileClip(media)
            try:
                clip = clip.save_frame(gggnefile, 0.1)
            except Exception:
                clip = clip.save_frame(gggnefile, 0)
    elif mediatype == "Document":
        mimetype = reply.document.mime_type
        mtype = mimetype.split("/")
        if mtype[0].lower() == "image":
            gggnemedia = await reply.download_media(file="./temp")
            im = Image.open(gggnemedia)
            im.save(gggnefile)
    if gggnemedia and os.path.lexists(gggnemedia):
        os.remove(gggnemedia)
    if os.path.lexists(gggnefile):
        return gggneevent, gggnefile, mediatype
    return gggneevent, None


async def take_screen_shot(
    video_file: str, duration: int, path: str = ""
) -> Optional[str]:
    thumb_image_path = path or os.path.join(
        "./temp/", f"{os.path.basename(video_file)}.jpg"
    )
    command = f"ffmpeg -ss {duration} -i '{video_file}' -vframes 1 '{thumb_image_path}'"
    err = (await runcmd(command))[1]
    if err:
        LOGS.error(err)
    return thumb_image_path if os.path.exists(thumb_image_path) else None
