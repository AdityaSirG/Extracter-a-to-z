# 🎓 UG Extractor Bot

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Pyrogram-2.0.106-green?style=for-the-badge&logo=telegram" />
  <img src="https://img.shields.io/badge/MongoDB-Motor-brightgreen?style=for-the-badge&logo=mongodb" />
  <img src="https://img.shields.io/badge/Deploy-Heroku-purple?style=for-the-badge&logo=heroku" />
</p>

<p align="center">
  एक powerful Telegram Bot जो online education platforms से course links extract करता है।
</p>

---

[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://dashboard.heroku.com/new?button-url=https://github.com/Cgps1234/newtxt)
                     

## ✨ Features

- 📚 **35+ Education Platforms** support
- 🔐 **Login / Without Login** दोनों modes
- 💎 **Premium System** with MongoDB
- 📄 **TXT → HTML** converter
- 🔒 **Code Encrypt / Decrypt** (`/enc`, `/dec`)
- 📢 **Broadcast System** (Admin only)
- 🌐 **Web Server** built-in (Heroku compatible)
- 🔄 **Auto Module Loading** system

---

## 📱 Supported Platforms

| Platform | Command | Mode |
|----------|---------|------|
| Physics Wallah (PW) | `/pw` | Login / Without Login |
| Classplus | `/cp` | Login |
| AppX / Appexams | `/appx` | Login / OTP |
| CareerWill | `/ugcw` | Login |
| Adda247 | `/adda` | Login |
| AK Competitions | `/ak` | Login |
| UTKarsh | `/utkarsh` | Login |
| KD Campus Live | `/kd` | Login |
| Khan Sir (My Pathshala) | `/my` | Login |
| IQ Education | `/iq` | Login |
| Exampur | — | Auto |
| Vision IAS | — | Auto |
| Mix / Other | — | Auto |
| RG Vikramjeet | `/rgvikramjeet` | Login |
| Free AppX | — | Auto |
| Free CP | — | Auto |
| Free PW | — | Auto |

---

## 🤖 Bot Commands

### 👤 User Commands
| Command | Description |
|---------|-------------|
| `/start` | Bot शुरू करो, menu देखो |
| `/myplan` | अपना premium plan check करो |
| `/txt2html` | TXT file को HTML में convert करो |
| `/html2txt` | HTML file को TXT में convert करो |
| `/enc` | Python file encrypt करो |
| `/dec` | Encrypted file decrypt करो |
| `/enchelp` | Encryption help देखो |

### 💎 Premium Commands
| Command | Description |
|---------|-------------|
| `/appxotp` | AppX OTP लो |
| `/getapi` | API find करो |
| `/sh` | Shell command |

### 🔧 Admin Only Commands
| Command | Description |
|---------|-------------|
| `/add_premium` | किसी को premium दो |
| `/remove_premium` | Premium हटाओ |
| `/premium_users` | सभी premium users देखो |
| `/chk_premium` | Premium check करो |
| `/broadcast` | सभी users को message भेजो |
| `/forward` | Message forward करो |
| `/announce` | Announcement करो |
| `/stats` | Bot statistics देखो |
| `/eval` | Python code run करो |

---

## ⚙️ Environment Variables (Config)

इन्हें Heroku `Config Vars` में या `.env` file में set करो:

| Variable | Description | Required |
|----------|-------------|----------|
| `API_ID` | Telegram API ID ([my.telegram.org](https://my.telegram.org)) | ✅ |
| `API_HASH` | Telegram API Hash | ✅ |
| `BOT_TOKEN` | Bot Token ([@BotFather](https://t.me/BotFather)) | ✅ |
| `BOT_USERNAME` | Bot का username (@ के साथ) | ✅ |
| `OWNER_ID` | Bot owner का Telegram User ID | ✅ |
| `CHANNEL_ID` | Log channel ID (जैसे `-1001234567890`) | ✅ |
| `CHANNEL_ID2` | Force subscribe channel ID | ✅ |
| `MONGO_URL` | MongoDB connection string | ✅ |
| `PREMIUM_LOGS` | Premium logs channel ID | ⚡ Optional |
| `THUMB_URL` | Default thumbnail image URL | ⚡ Optional |

---

## 🚀 Deploy करो

### Method 1 — Heroku पर Deploy

1. [Heroku](https://heroku.com) पर account बनाओ
2. नया App बनाओ
3. **Settings → Config Vars** में सभी variables add करो (ऊपर table देखो)
4. **Deploy → GitHub** से connect करो या Heroku CLI use करो:

```bash
heroku login
heroku git:remote -a YOUR_APP_NAME
git push heroku main
```

5. **Resources** tab में `worker` dyno enable करो:
```
worker: python -m Extractor
```

---

### Method 2 — VPS / Local पर Run

**Step 1 — Clone करो**
```bash
git clone https://github.com/YOUR_REPO/Extractor
cd Extractor
```

**Step 2 — Python 3.10 install करो**
```bash
sudo apt install python3.10 python3-pip -y
```

**Step 3 — Dependencies install करो**
```bash
pip install -r requirements.txt
```

**Step 4 — Environment variables set करो**

`.env` file बनाओ:
```env
API_ID=12345678
API_HASH=your_api_hash_here
BOT_TOKEN=your_bot_token_here
BOT_USERNAME=@YourBotUsername
OWNER_ID=123456789
CHANNEL_ID=-1001234567890
CHANNEL_ID2=-1001234567890
MONGO_URL=mongodb+srv://user:pass@cluster.mongodb.net/
PREMIUM_LOGS=-1001234567890
THUMB_URL=https://example.com/thumb.jpg
```

**Step 5 — Bot start करो**
```bash
python run.py
```

या directly:
```bash
python -m Extractor
```

---

## 📁 Project Structure

```
Extractor/
│
├── Extractor/
│   ├── __init__.py          # Pyrogram Client (app) initialize
│   ├── __main__.py          # Bot entry point, modules loader
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── func.py          # subscribe(), chk_user() helpers
│   │   ├── script.py        # Bot text messages (START_TXT, FORCE_MSG आदि)
│   │   ├── utils.py         # forward_to_log() utility
│   │   └── mongo/
│   │       ├── plans_db.py  # Premium users DB functions
│   │       └── usersdb.py   # Users DB functions
│   │
│   └── modules/
│       ├── __init__.py      # Auto module loader (ALL_MODULES)
│       ├── start.py         # /start, main menu handlers
│       ├── bot.py           # TXT→HTML converter handler
│       ├── broadcast.py     # /broadcast, /forward, /announce
│       ├── plans.py         # Premium system commands
│       ├── stats.py         # /stats command
│       ├── enc.py           # /enc, /dec, /enchelp
│       ├── eval.py          # /eval command
│       ├── check.py         # Premium check
│       ├── server.py        # Web server (Heroku ping)
│       ├── botenc.py        # Encrypted bot module
│       ├── adda.py          # Adda247 extractor
│       ├── ak.py            # AK Competitions extractor
│       ├── appex_v1.py      # AppX v1 extractor
│       ├── appex_v2.py      # AppX v2 extractor
│       ├── appex_v3.py      # AppX v3 extractor
│       ├── appex_v4.py      # AppX v4 extractor
│       ├── careerwill.py    # CareerWill extractor
│       ├── classplus.py     # Classplus extractor
│       ├── exampur.py       # Exampur extractor
│       ├── findapi.py       # API finder
│       ├── freeappx.py      # Free AppX extractor
│       ├── freecp.py        # Free Classplus extractor
│       ├── freepw.py        # Free PW extractor
│       ├── getappxotp.py    # AppX OTP handler
│       ├── iq.py            # IQ Education extractor
│       ├── kdlive.py        # KD Live extractor
│       ├── khan.py          # Khan Sir extractor
│       ├── mix.py           # Mixed platforms extractor
│       ├── mypathshala.py   # My Pathshala extractor
│       ├── pw.py            # Physics Wallah extractor
│       ├── rg_vikramjeet.py # RG Vikramjeet extractor
│       ├── utk.py           # UTKarsh extractor
│       └── vision.py        # Vision IAS extractor
│
├── config.py                # सभी config variables
├── run.py                   # App launcher (local + Heroku)
├── secure.py                # Python file encryptor/decryptor (CLI tool)
├── requirements.txt         # Python dependencies
├── runtime.txt              # python-3.10.11
└── Procfile                 # Heroku process definition
```

---

## 📦 Requirements

```
pyrogram==2.0.106
pyromod==1.5
tgcrypto
aiohttp
aiofiles
requests
hachoir
cloudscraper
pycryptodome
pytz
motor
pyrofork
PyJWT
aiogram
beautifulsoup4
httpx
python-telegram-bot==20.6
tqdm
colorama
termcolor
python-dotenv
```

---

## 🔐 Login Format

Platforms जो login support करती हैं:

```
ID*Password
```

**Example:**
```
9769696969*mypassword123
```

या directly token:
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

---

## 💎 Premium Plans

| Plan | Duration | Price |
|------|----------|-------|
| 🎁 Free Trial | 5 Minutes | Free |
| 🥉 Bronze | 7 Days | ₹300 |
| 🥈 Silver | 15 Days | ₹500 |
| 🥇 Gold | 30 Days | ₹800 |
| 🎯 Custom | अपनी choice | Days के हिसाब से |

Premium add करने के लिए Admin से contact करो।

---

## 🛠️ Admin: Premium Manage करना

**Premium देना:**
```
/add_premium USER_ID DAYS
```

**Premium हटाना:**
```
/remove_premium USER_ID
```

**सभी premium users देखना:**
```
/premium_users
```

---

## 🔒 secure.py — Code Encryptor (CLI Tool)

यह एक standalone CLI tool है, bot module नहीं।

```bash
python secure.py
```

- अपनी `.py` file का path दो
- Encrypt या Decrypt choose करो
- Output file automatically save होगी

---

## ⚠️ Important Notes

- Bot run करने से पहले सभी **Config Vars** जरूर set करो
- MongoDB Atlas पर free cluster बना सकते हो: [mongodb.com](https://www.mongodb.com/atlas)
- Log channel में bot को **Admin** बनाओ
- Force subscribe channel में bot को **Admin** बनाओ
- `sessions/` folder automatically create होगा

---

## 📞 Support

- **Owner:** [@UGxPro](https://t.me/UGxPro)
- **Support Group:** [@DevsOops](https://t.me/DevsOops)
- **Updates Channel:** [@UGBotx](https://t.me/UGBotx)

---

## 📜 License

इस project को **LICENSE** file के अनुसार use करें।

---

<p align="center">Made with ❤️ by UG Team</p>
