# Sirf /tagall (poore members) ke liye. Apne PHONE/Termux pe chalao, Render pe nahi.
#   pip install telethon
#   python gen_session.py
# API ID / API HASH: my.telegram.org -> API development tools
# Ye SPARE account se banao (main account se nahi). Jo string niklegi wo account ka password jaisi he,
# kisi ko mat dena - sirf Render/Railway ke STRING_SESSION variable me daalo.
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

api_id = int(input("API ID: ").strip())
api_hash = input("API HASH: ").strip()
with TelegramClient(StringSession(), api_id, api_hash) as client:
    print("\nSTRING_SESSION =\n" + client.session.save())
