from telethon import events
from datetime import datetime
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="ping ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    await event.delete()
    start = datetime.now()
    mone = await event.reply("\n My 🇵 🇮 🇳 🇬  Is : Calculating...")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await mone.edit(" \n My 🇵 🇮 🇳 🇬  Is : {}".format(ms))
 
