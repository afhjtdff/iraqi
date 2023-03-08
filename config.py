from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = os.environ.get("22650873")
APP_HASH = os.environ.get("173709fd95c4a06fa0005fd966dc8ef8")
BOT_USERNAME = os.environ.get("brhdhdhrjbot")
session = os.environ.get("1ApWapzMBu5pAUXG4Av3VcRRADdy6l1oUgpLmtIHdcmIjOHqG7Q9zPtpcI2EK7SlvQ3NSxn2V97ICfHvhs0yfziNu14joa5jmv51MyNnxzEv3tn3aw-ykf7uhDhJo7SzP_VcNyOM-8pGnBJQlU3n-3MC-z7IRRiVKMweO5tuL6E0RVeELh83IAjJEC68PwzIcL_F2XkvlAtFPUhpB6JQdvqjpts0HNWmjdkjAiBtzravPThnUOXctzDHHsAIVuSxb-FeiweCXoUk5hYm7BoUkYYvEI7bWa98DnEwYYCxZskIuECxmShcSjRzSE3Pnv7208j4fYhMIJbMFOhxJp7L3I0hUnKecc0c=")
SESSION = os.environ.get("1ApWapzMBu5pAUXG4Av3VcRRADdy6l1oUgpLmtIHdcmIjOHqG7Q9zPtpcI2EK7SlvQ3NSxn2V97ICfHvhs0yfziNu14joa5jmv51MyNnxzEv3tn3aw-ykf7uhDhJo7SzP_VcNyOM-8pGnBJQlU3n-3MC-z7IRRiVKMweO5tuL6E0RVeELh83IAjJEC68PwzIcL_F2XkvlAtFPUhpB6JQdvqjpts0HNWmjdkjAiBtzravPThnUOXctzDHHsAIVuSxb-FeiweCXoUk5hYm7BoUkYYvEI7bWa98DnEwYYCxZskIuECxmShcSjRzSE3Pnv7208j4fYhMIJbMFOhxJp7L3I0hUnKecc0c=")
token = os.environ.get("5731752690:AAGKGW4NXRIpBx7tvqopP1IT-kG8ATJJCkw")
fifthon = TelegramClient(StringSession(session), APP_ID, APP_HASH)
bot = TelegramClient("bot", APP_ID, APP_HASH).start(bot_token=token)
ispay = ['yes']
ispay2 = ['yes']
bot.start()
