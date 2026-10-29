# gen_sessions.py - DO alag session banata he (har bot ke liye ek). Termux me chalao: python gen_sessions.py
# API ID / API HASH: my.telegram.org -> API development tools
# NIYAM: ek session = ek hi jagah. Ek string 2 bots me daaloge to Telegram use maar deta he.
# Ye strings account ke password jaisi hain: chat me mat bhejna.
# Script ko baar baar mat chalao: har baar Telegram naya code bhejta he aur kuch der ke liye rok deta he.
import asyncio
import base64
import struct

from telethon import TelegramClient
from telethon.errors import (FloodWaitError, PhoneCodeExpiredError, PhoneCodeInvalidError,
                             SessionPasswordNeededError)
from telethon.sessions import StringSession


def pyrogram_string(dc_id, api_id, auth_key, user_id):
    raw = struct.pack(">BI?256sQ?", dc_id, api_id, False, auth_key, user_id, False)
    return base64.urlsafe_b64encode(raw).decode().rstrip("=")


async def login(api_id, api_hash):
    c = TelegramClient(StringSession(), api_id, api_hash)
    await c.connect()
    phone = input("Phone number (+91 ke saath): ").strip()
    for _ in range(3):
        try:
            sent = await c.send_code_request(phone)
        except FloodWaitError as e:
            print("\nTelegram ne roka he. %d minute baad dobara try karo." % (e.seconds // 60 + 1))
            return None
        token = getattr(sent, "phone_code_hash", "") or ""
        if not token:
            print("\nTelegram ne abhi code ka token nahi diya (pichla code abhi active he).")
            print("-> 10 minute ruko, phir script sirf EK baar chalao.")
            return None
        code = input("Telegram app me aaya code: ").strip().replace(" ", "").replace("-", "")
        try:
            await c.sign_in(phone, code, phone_code_hash=token)
            return c
        except SessionPasswordNeededError:
            await c.sign_in(password=input("2-step verification password: "))
            return c
        except PhoneCodeInvalidError:
            print("Code galat tha, naya code bhej raha hu...")
        except PhoneCodeExpiredError:
            print("Code expire ho gaya, naya code bhej raha hu...")
    print("3 baar me login nahi hua. Thodi der baad dobara try karo.")
    return None


async def main():
    api_id = int(input("API ID: ").strip())
    api_hash = input("API HASH: ").strip()
    for n in (1, 2):
        print("\n===== SESSION %d =====" % n)
        c = await login(api_id, api_hash)
        if not c:
            print("SESSION %d nahi bana." % n)
            continue
        me = await c.get_me()
        print("\nLogin hua: %s" % (me.first_name or me.id))
        print("\n[TELETHON string] -> Ruhi bot (STRING_SESSION) ya Telethon wale bot ke liye:\n" + c.session.save())
        print("\n[PYROGRAM string] -> sirf Pyrogram wale bot ke liye:\n" +
              pyrogram_string(c.session.dc_id, api_id, c.session.auth_key.key, me.id))
        print("\nDhyan: SESSION %d ki ek hi string (Telethon YA Pyrogram) ek hi bot me lagani he." % n)
        await c.disconnect()


asyncio.run(main())
