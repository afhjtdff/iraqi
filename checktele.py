import random
import threading
import asyncio
import telethon
from telethon import events
from queue import Queue
import requests
from telethon.sync import functions
from user_agent import generate_user_agent
import requests
from user_agent import *
from help import *
from config import *
from threading import Thread

a = 'qwertyuiopassdfghjklzxcvbnm'
b = '1234567890'
e = 'qwertyuiopassdfghjklzxcvbnm1234567890'

banned = []
isclaim = ["off"]
isauto = ["off"]
with open("banned.txt", "r") as f:
    f = f.read().split()
    banned.append(f)

que = Queue()


def check_user(username):
    url = "https://t.me/"+str(username)
    headers = {
        "User-Agent": generate_user_agent(),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}

    response = requests.get(url, headers=headers)
    if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
        return "Available"
    else:
        return "Unavailable"

def gen_user(choice):
    if choice == "1":
        c = random.choices(a)
        d = random.choices(b)
        s = random.choices(e)
        f = [c[0], "_", d[0], "_", s[0]]
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(b)
            s = random.choices(e)
            f = [c[0], "_", d[0], "_", s[0]]
            username = ''.join(f)
        else:
            pass
    if choice == "2":
        c = random.choices(a)
        d = random.choices(a)
        s = random.choices(e)
        f = [c[0], "_", d[0], "_", s[0]]
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(b)
            s = random.choices(e)
            f = [c[0], "_", d[0], "_", s[0]]
            username = ''.join(f)
        else:
            pass
    if choice == "3":
        c = random.choices(a)
        d = random.choices(b)
        s = random.choices(e)
        f = [c[0], s[0]]
        random.shuffle(f)
        username = ''.join(f)
        username = username+'bot'
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(b)
            s = random.choices(e)
            f = [c[0], s[0]]
            random.shuffle(f)
            username = ''.join(f)
            username = username+'bot'
        else:
            pass
    if choice == "4":
        c = random.choices(a)
        d = random.choices(b)
        s = random.choices(e)
        f = [c[0], s[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        username = username+'bot'
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(b)
            s = random.choices(e)
            f = [c[0], s[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
            username = username+'bot'
        else:
            pass
    if choice == "5":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], c[0], c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], c[0], c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "6":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], c[0], c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "7":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], c[0], c[0], c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "8":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], c[0], c[0], c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "9":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], c[0], d[0], c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], c[0], c[0], d[0], c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "10":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], "_", c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], "_", c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    return username

@fifthon.on(events.NewMessage(outgoing=True, pattern=r"\.تشيكر"))
async def _(event):
    if ispay2[0] == "yes":
        await event.edit(tele_checker)
        
@fifthon.on(events.NewMessage(outgoing=True, pattern=r"\.اليوزرات المبندة"))
async def _(event):
    if ispay2[0] == "yes":
        await fifthon.send_file(event.chat_id, 'banned.txt')


@fifthon.on(events.NewMessage(outgoing=True, pattern=r"\.الانواع"))
async def _(event):
    if ispay2[0] == "yes":
        await event.edit(tele_checker2)
# صيد عدد نوع قناة


@fifthon.on(events.NewMessage(outgoing=True, pattern=r"\.صيد (.*)"))
async def _(event):
    if ispay2[0] == "yes":
        isclaim.clear()
        isclaim.append("on")
        msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 2)
        ch = str(msg[2])
        choice = str(msg[1])
        trys = 0
        await event.edit(f"𝙬𝙚𝙡𝙡 𝙘𝙝𝙚𝙘𝙠 𝙤𝙪𝙩 𝙩𝙮𝙥𝙚 𓅃 `{choice}` 𝙁𝙍𝙊𝙈 𝙐𝙎𝙀𝙍𝙉𝘼𝙈𝙀 𝙊𝙉 `{ch}` , 𝘽𝙔 𝙉𝙐𝙈𝘽𝙀𝙍  `{msg[0]}` 𝙊𝙁 𝘼𝙏𝙏𝙀𝙈𝘽𝙏𝙎")

        @fifthon.on(events.NewMessage(outgoing=True, pattern=r"\.حالة الصيد"))
        async def _(event):
            if ispay2[0] == "yes":
                if "on" in isclaim:
                    await event.edit(f"𝙏𝙃𝙀 𝘾𝙃𝙀𝘾𝙆 𝘼𝙍𝙍𝙄𝙑𝙀𝘿({trys}) 𝙊𝙁 𝘼𝙏𝙏𝙀𝙈𝙋𝙏𝙎")
                elif "off" in isclaim:
                    await event.edit("𝙏𝙃𝙀 𝘾𝙃𝙀𝘾𝙆𝙀𝙍 𝙎𝙏𝙊𝙋𝙋𝙀𝘿 ✪ !")
                else:
                    await event.edit("خطأ")
            else:
                pass
        for i in range(int(msg[0])):
            if ispay2[0] == 'no':
                break
            username = ""

            username = gen_user(choice)
            t = Thread(target=lambda q, arg1: q.put(
                check_user(arg1)), args=(que, username))
            t.start()
            t.join()
            isav = que.get()
            if "Available" in isav:
                await asyncio.sleep(1)
                try:
                    await fifthon(functions.channels.UpdateUsernameRequest(
                        channel=ch, username=username))
                    await event.client.send_message(event.chat_id, f'''
♡𝙞𝙧𝙖𝙦 ~~ @isiraqi ♡ 
✿❯────「✿」────❮✿

𓆩@{𝙪𝙨𝙚𝙧𝙖𝙢𝙚}!
   {trys}
❦ ════ •⊰❂⊱• ════ ❦
𓆩𝘾𝙊𝙉𝙂𝙍𝘼𝙏𝙐𝙇𝘼𝙏𝙄𝙊𝙉𝙎 ♡

≪━─━─━─━─◈─━─━─♡

    ''')
                    break
                except telethon.errors.rpcerrorlist.UsernameInvalidError:
                    with open("banned.txt", "a") as f:
                        f.write(f"\n{username}")
                except Exception as eee:
                    await fifthon.send_message(event.chat_id, f'''𝙒𝙍𝙊𝙉𝙂 𝙒𝙞𝙩𝙝 🔱  @{username}
    الخطأ :
    {str(eee)}''')
                    if "A wait of" in str(eee):
                        break
                    else:
                        await fifthon.send_message(event.chat.id, "  𝙏𝙃𝙄𝙎 𝙁𝙍𝙀𝙀 𝙏𝙍𝙔 𝙒𝙄𝙏𝙃 𝙔𝙊𝙐 ◉ !")
            else:
                pass
            trys += 1

        isclaim.clear()
        isclaim.append("off")
        trys = ""
        await event.client.send_message(event.chat_id, "𝗙𝗜𝗦𝗛𝗜𝗡𝗚 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗")
        
@fifthon.on(events.NewMessage(outgoing=True, pattern=r"\.تثبيت (.*)"))
async def _(event):
    if ispay2[0] == "yes":
        trys = 0
        msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
        if msg[0] == "تلقائي":  # تثبيت تلقائي عدد يوزر قناة
            isauto.clear()
            isauto.append("on")
            msg = ("".join(event.text.split(maxsplit=2)[2:])).split(" ", 2)
            username = str(msg[2])
            ch = str(msg[1])
            await event.edit(f"𝙬𝙚𝙡𝙡 𝙘𝙝𝙚𝙘𝙠 `{username}` 𝙊𝙉 `{ch}` , بعدد `{msg[0]}` 𝙊𝙁 𝘼𝙏𝙏𝙀𝙈𝘽𝙏𝙎 !")

            @fifthon.on(events.NewMessage(outgoing=True, pattern=r"\.حالة التثبيت التلقائي"))
            async def _(event):
                if "on" in isauto:
                    msg = await event.edit(f"التثبيت وصل لـ({trys}) من المحاولات")
                elif "off" in isauto:
                    await event.edit("لايوجد تثبيت شغال !")
                else:
                    await event.edit("خطأ")
            for i in range(int(msg[0])):
                if ispay2[0] == 'no':
                    break
                t = Thread(target=lambda q, arg1: q.put(
                    check_user(arg1)), args=(que, username))
                t.start()
                t.join()
                isav = que.get()
                if "Available" in isav:
                    try:
                        await fifthon(functions.channels.UpdateUsernameRequest(
                            channel=ch, username=username))
                        await event.client.send_message(event.chat_id, f'''
♡𝙞𝙧𝙖𝙦 ~~ @F_3_3 ♡ 
✿❯────「✿」────❮✿

𓆩@{𝙪𝙨𝙚𝙧𝙖𝙢𝙚}!

  {trys}
❦ ════ •⊰❂⊱• ════ ❦
𓆩𝘾𝙊𝙉𝙂𝙍𝘼𝙏𝙐𝙇𝘼𝙏𝙄𝙊𝙉𝙎 ♡༒

≪━─━─━─━─◈─━─━─♡

    ''')
                        break
                    except telethon.errors.rpcerrorlist.UsernameInvalidError:
                        await event.client.send_message(event.chat_id, f"مبند `{username}` ❌❌")
                        break
                    except Exception as eee:

                        await fifthon.send_message(event.chat_id, f'''خطأ مع {username}
    الخطأ :
    {str(eee)}''')
                        if "A wait of" in str(eee):
                            break
                else:
                    pass
                trys += 1

                await asyncio.sleep(8)
            trys = ""
            isclaim.clear()
            isclaim.append("off")
            await fifthon.send_message(event.chat_id, "𝗙𝗜𝗦𝗛𝗜𝗡𝗚 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗")
        if msg[0] == "يدوي":  # تثبيت يدوي يوزر قناة
            await event.edit(f"حسناً سأحاول تثبيت `{username}` على `{ch}` !")
            msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
            username = str(msg[0])
            ch = str(msg[1])
            try:
                await fifthon(functions.channels.UpdateUsernameRequest(
                    channel=ch, username=username))
                await event.client.send_message(event.chat_id, f'''
♡𝙞𝙧𝙖𝙦 ~~ @F_3_3 ♡ 
✿❯────「✿」────❮✿

𓆩@{𝙪𝙨𝙚𝙧𝙖𝙢𝙚}!

  {trys}
❦ ════ •⊰❂⊱• ════ ❦
𓆩𝘾𝙊𝙉𝙂𝙍𝘼𝙏𝙐𝙇𝘼𝙏𝙄𝙊𝙉𝙎 ♡

≪━─━─━─━─◈─━─━─♡
    ''')
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                await event.client.send_message(event.chat_id, f"مبند `{username}` ❌❌")
            except Exception as eee:
                await fifthon.send_message(event.chat_id, f'''خطأ مع {username}
    الخطأ :
    {str(eee)}''')
Threads=[] 
for t in range(100):
    x = threading.Thread(target=_)
    le = threading.Thread(target=gen_user)
    x.start()
    le.start()
    Threads.append(x)
    Threads.append(le)
for Th in Threads:
    Th.join()
