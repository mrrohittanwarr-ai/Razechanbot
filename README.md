# Raze Chan (Ruhi) AI Bot  —  @obito_space

Group management + Gen-Z AI chat + /anime + fonts + sticker replies + daily-renewing invite link.
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
6. `/setdub naruto | Hindi | #Official | 480p, 720p, 1080p` - jis anime ka audio/quality tum jaante ho wo daalo. Baaki anime ke liye wahi default dikhega jo `/set anime_audio` me he.

## Dhyan rakhne wali baatein
- AI ko user ka naam/ID/username/phone/link nahi jata (scrub hota he). Chat history sirf RAM me rehti he, restart pe mit jati he.
- Bot khud ko insaan nahi bolega agar koi sach me pooche "bot ho?" - ye rule hata nahi sakte `/set persona` se.
- `/utag` sirf unhe tag karta he jo bot ne group me bolte dekha (Telegram bots poori member list nahi dekh sakte).
- Link badalne se purani link band ho jati he - purane DM wale button ko dobara /start karna padega.
- Self-learning: bot har 12 ghante me chat style ke tips banata he aur **tumse permission** maangta he. Bina approve kiye kuch nahi seekhta.
