# Raze Chan (Ruhi) AI Bot  —  @obito_space

Group management + Gen-Z AI chat + anime post filter + fonts + sticker replies + daily-renewing invite link.
Code me kuch edit nahi karna: sab kuch bot ke andar `/set`, `/setdefault`, `/addpack` jaise commands se badalta hai.

## 1) Pehle ye 4 cheezein banao
1. **Bot token** - @BotFather → /newbot.
   Phir **/setprivacy → Disable** (ZARURI: warna filters, naam se bulana aur tagging group me kaam nahi karenge).
2. **MongoDB** - mongodb.com/atlas → free cluster → Database Access me user banao → Network Access me `0.0.0.0/0` allow → "Connect → Drivers" se `MONGO_URI` copy karo.
3. **AI key** - Oxion dashboard → API Keys.
4. **Apna numeric ID** - @userinfobot ko /start karo → `OWNER_ID`.

## 2) Deploy (koi ek)
**Render (free):** GitHub pe ye 5 files daalo → Render → New → Web Service → repo chuno → Runtime **Docker** → Environment me `.env.example` ke 4 zaroori variables daalo.
Free service 15 min baad so jati hai: service ka URL `KEEPALIVE_URL` me daalo **aur** uptimerobot.com pe us URL ka 5-min ping monitor bhi laga do.

**Railway:** New Project → Deploy from GitHub → variables daalo (Dockerfile apne aap pakad leta hai).

**VPS (dost wala):**
```
docker build -t ruhibot .
docker run -d --restart unless-stopped --env-file .env --name ruhibot ruhibot
```

## 3) Pehli baar setup (sab Telegram ke andar)
1. Bot ko DM karo `/help` → owner commands dikhenge.
2. `/models` → koi bada model chuno (Kimi/GLM jaisa) → `/set model <id>`. `/aistatus` se test karo.
3. Apne group me bot ko **admin** banao (delete, ban/restrict, pin, **invite users** permission) → group me `/setdefault`.
   Ab DM me `/start` karne wale ko tumhare group ki link milegi jo har ~24 ghante me nayi ban jati he.
4. Stickers: apna sticker pack bana ke `/addpack <pack_naam>`.
5. Personality: `/set persona <text>` (lamba text ho to pehle ek msg me likho, usko reply karke `/set persona`).
6. **Anime posts:** apni post (button/link ke saath) bot ko DM me forward karo. Post ki pehli line ka naam (jaise `Naruto: Shippuden [S18]`) apne aap filter ban jata he. Ab group ya DM me `Naruto Shippuden` likhne par wahi post, usi formatting, link aur button ke saath aati he. `/posts` list, `/delpost <naam>` hatane ke liye, `/addpost <naam>` (post ko reply karke) alag naam dene ke liye.
7. **/tagall (sab members):** assistant ke bina `/tagall` sirf unhe tag karta he jo bot ne dekhe. Poore members ke liye spare Telegram account se `gen_sessions.py` chalao aur `TG_API_ID`, `TG_API_HASH`, `STRING_SESSION` env me daalo. Wo spare account group ka member hona chahiye.

## Dhyan rakhne wali baatein
- AI ko user ka naam/ID/username/phone/link nahi jata (scrub hota he). Chat history sirf RAM me rehti he, restart pe mit jati he.
- Bot khud ko insaan nahi bolega agar koi sach me pooche "bot ho?" - ye rule hata nahi sakte `/set persona` se.
- Telegram bots poori member list nahi dekh sakte, isliye `/utag` sirf dekhe hue members tag karta he. Poore ke liye assistant account (step 7). Dhyan: user account se automation Telegram ke rules me grey area he, ban ho sakta he, isliye sirf spare account.
- Link badalne se purani link band ho jati he - purane DM wale button ko dobara /start karna padega.
- Self-learning: bot har 12 ghante me chat style ke tips banata he aur **tumse permission** maangta he. Bina approve kiye kuch nahi seekhta.

## AI (Oxion / Gemini / Grok) - sab bot ke andar se
- **Env me** `GROQ_API_KEY` (gsk_...) aur `GEMINI_API_KEY` daal do - bot khud pehle Groq, phir Gemini, phir Oxion (`AI_API_KEY`) try karta he. Model apne aap chun leta he.
- `/setkey <key>` - default (Oxion) key. Msg apne aap delete ho jata he.
- `/addai gemini <key>` - Gemini jodo (Google AI Studio ki key, free tier). Model apne aap chun leta he. **Sirf DM me.**
- `/addai grok <key>` - Grok (xAI). Dhyan: Grok API free nahi, prepaid credit lagta he.
- `/ais` list, `/useai <naam>` pehle kaunsa (`/useai auto` = wapas normal order), `/aimodel <naam> <model>`, `/delai <naam>`, `/models [naam]`, `/aistatus` test.
- Jo pehla wala band ho jaye to bot khud agle provider se jawab de deta he.
- Group me bot pichle `/set context 4` msg padh ke reply karta he. `/set temperature 0.9` se uski masti badlo.

## Anime index
Group ya DM me sirf `/anime` likho: saare saved anime A-Z me, har naam ke andar uska link. Is msg ko forward karke apne channel ke top pe daal sakte ho.

## /tagall nahi chal raha?
DM me `/assistant` chalao - wo bata deta he kya kami he (env variable, telethon, session). Pyrogram wali string bhi chalti he, bot use convert kar leta he.

## Broadcast + pinned start
- `/broadcast <text>` (sirf DM me, sirf owner) - pehle preview + "Bhejo/Cancel" aata he, tab jata he. Photo/video bhejna ho to us msg ko reply karke `/broadcast`.
  Jo bot ko block kar chuke ya kabhi start nahi kiya unhe apne aap skip karta he (wapas likhein to dobara judte hain).
- DM me `/start` wala message user ke chat me pin ho jata he. Band karna ho: `/set pin_start off`.

## Reply style
- Ruhi ab sirf **ek line** me jawab deti he, aadhe replies me hi emoji. `/set persona default` se nayi personality lag jati he.
- Acchi settings: `/set temperature 0.8`, `/set context 5`, `/set names off`.

## Alag anime list har group ke liye
- Pehli (default) list ka naam `@Crunchyrollchannel` he. Ye saare groups aur DM me chalti he, siwaye un groups ke jinki apni list bani ho.
- `/addanimelist <group_id> [naam]` (DM me) - us group ke liye nayi list. Naam nahi diya to bot pooch leta he. Group ki id group me `/id` likhne se milti he.
  Ban-ne ke baad jo bhi anime forward karoge wo isi list me jayenge.
- `/listset` - sab lists + ON/OFF button + 🎯 (forward kahan jaye). Ek saath kitni bhi lists ON rakh sakte ho.
- `/setlist <naam>` forward ki list badlo, `/dellist <naam>` list hatao (confirm lagta he), `/posts` abhi wali list ke anime.
- Jis group ki apni list OFF kar do, wahan kuch nahi dikhega (default list nahi aayegi).

## Gussa mode
- `/set gussa mild` (default) ya `/set gussa off`. Mild me badtameezi par gussa aur halki gaali (pagal, ullu, bewakoof...). Maa-behen, jaati-dharm, body, sexual gaali kabhi nahi; udaas ya chhote user par bilkul nahi.
