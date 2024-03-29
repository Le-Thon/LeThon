import os
import subprocess
from datetime import datetime

from gtts import gTTS

from gggne import gggne

from ..core.managers import edit_delete, edit_or_reply
from . import deEmojify, reply_id


@gggne.ar_cmd(pattern="انطق(?:\s|$)([\s\S]*)")
async def _(event):
    input_str = event.pattern_match.group(1)
    start = datetime.now()
    reply_to_id = await reply_id(event)
    if ";" in input_str:
        lan, text = input_str.split(";")
    elif event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str or "ar"
    else:
        if not input_str:
            return await edit_or_reply(event, "- هذا نص غير صحيح")
        text = input_str
        lan = "ar"
    gggneevent = await edit_or_reply(event, "⌔∮ جـار التسجيل انتـظر قليلا")
    text = deEmojify(text.strip())
    lan = lan.strip()
    if not os.path.isdir("./temp/"):
        os.makedirs("./temp/")
    required_file_name = "./temp/" + "voice.ogg"
    try:
        tts = gTTS(text, lang=lan)
        tts.save(required_file_name)
        command_to_execute = [
            "ffmpeg",
            "-i",
            required_file_name,
            "-map",
            "0:a",
            "-codec:a",
            "libopus",
            "-b:a",
            "100k",
            "-vbr",
            "on",
            required_file_name + ".opus",
        ]
        try:
            t_response = subprocess.check_output(
                command_to_execute, stderr=subprocess.STDOUT
            )
        except (subprocess.CalledProcessError, NameError, FileNotFoundError) as exc:
            await gggneevent.edit(str(exc))
        else:
            os.remove(required_file_name)
            required_file_name = required_file_name + ".opus"
        end = datetime.now()
        ms = (end - start).seconds
        await event.client.send_file(
            event.chat_id,
            required_file_name,
            reply_to=reply_to_id,
            allow_cache=False,
            voice_note=True,
        )
        os.remove(required_file_name)
        await edit_delete(
            gggneevent,
            "تحويل النص {} الى مقطع صوتي في {} ثواني ".format(text[0:20], ms),
        )
    except Exception as e:
        await edit_or_reply(gggneevent, f"**خطأ:**\n`{e}`")
