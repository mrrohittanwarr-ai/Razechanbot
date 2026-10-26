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
7. **/tagall (sab members):** assistant ke bina `/tagall` sirf unhe tag karta he jo bot ne dekhe. Poore members ke liye spare Telegram account se `gen_session.py` chalao aur `TG_API_ID`, `TG_API_HASH`, `STRING_SESSION` env me daalo. Wo spare account group ka member hona chahiye.

## Dhyan rakhne wali baatein
- AI ko user ka naam/ID/username/phone/link nahi jata (scrub hota he). Chat history sirf RAM me rehti he, restart pe mit jati he.
- Bot khud ko insaan nahi bolega agar koi sach me pooche "bot ho?" - ye rule hata nahi sakte `/set persona` se.
- Telegram bots poori member list nahi dekh sakte, isliye `/utag` sirf dekhe hue members tag karta he. Poore ke liye assistant account (step 7). Dhyan: user account se automation Telegram ke rules me grey area he, ban ho sakta he, isliye sirf spare account.
- Link badalne se purani link band ho jati he - purane DM wale button ko dobara /start karna padega.
- Self-learning: bot har 12 ghante me chat style ke tips banata he aur **tumse permission** maangta he. Bina approve kiye kuch nahi seekhta.
