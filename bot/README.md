# 🤖 SoulLight Academy – Telegram Bot

Vollständiger Telegram-Bot für die SoulLight Academy mit automatisierten Affirmationen, Buchungssystem, Meditationen, FAQ und Premium-Community-Verwaltung.

---

## 📋 Features

| Feature | Beschreibung |
|---------|-------------|
| `/start` | Willkommensnachricht + interaktives Hauptmenü |
| `/angebote` | Alle 4 Dienstleistungen mit Details & Preisen |
| `/pakete` | Premium-Pakete (Erwachen / Befreiung / Seelenreise VIP) |
| `/buchen` | Buchungsprozess mit Weiterleitung zu Cal.com |
| `/meditation` | Zufällige geführte Meditation |
| `/affirmation` | Zufällige Tagesaffirmation |
| `/faq` | Häufig gestellte Fragen (interaktiv) |
| `/kontakt` | Kontaktdaten & direkte Nachricht an Admin |
| `/premium` | Inner Circle Infos + Stripe-Zahlungslink |
| **Auto-Affirmation** | Jeden Morgen um 7:00 in der Free-Gruppe |
| **Premium-Impuls** | Jeden Morgen um 8:00 in der Premium-Gruppe |
| **Willkommen** | Automatische Begrüßung neuer Gruppenmitglieder |
| **Nachrichten-Weiterleitung** | Freitext → wird an Admin weitergeleitet |

---

## 🚀 Setup-Anleitung (Schritt für Schritt)

### 1️⃣ Bot bei Telegram erstellen

1. Öffne Telegram und suche **@BotFather**
2. Schreibe `/newbot`
3. Wähle einen Namen: `SoulLight Academy`
4. Wähle einen Username: `SoulLightAcademyBot` (muss auf `Bot` enden)
5. **Kopiere den Token** – den brauchst du gleich!

**Zusätzlich bei @BotFather:**
```
/setdescription → Dein Raum für spirituelle Heilung ✨
/setabouttext   → Hypnose | Karmaauflösung | Rückführung | Spirit Healing
/setcommands    → 
start - Hauptmenü
angebote - Unsere Dienstleistungen
pakete - Premium-Pakete
buchen - Termin buchen
premium - Inner Circle beitreten
meditation - Geführte Meditation
affirmation - Tagesaffirmation
faq - Häufige Fragen
kontakt - Kontaktdaten
hilfe - Alle Befehle
```

### 2️⃣ Python installieren

- Lade Python 3.10+ von https://www.python.org herunter
- Bei der Installation: ✅ **"Add Python to PATH"** ankreuzen!

### 3️⃣ Bot einrichten

```bash
# In den Bot-Ordner wechseln
cd bot

# Pakete installieren
pip install -r requirements.txt

# Konfiguration erstellen
copy .env.example .env
```

### 4️⃣ `.env` Datei ausfüllen

Öffne die `.env` Datei und trage deine Daten ein:

```env
BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrsTUVwxyz    ← von @BotFather
FREE_GROUP_ID=-1001234567890                        ← deine Gruppen-ID
PREMIUM_GROUP_ID=-1001234567891                     ← Premium-Gruppe
ADMIN_USER_ID=123456789                             ← deine User-ID
BOOKING_URL=https://cal.com/dein-name               ← dein Buchungslink
```

**Wie bekomme ich die IDs?**
- **Deine User-ID:** Schreibe `@userinfobot` an auf Telegram
- **Gruppen-ID:** Füge `@RawDataBot` zur Gruppe hinzu → er zeigt die ID

### 5️⃣ Bot starten

```bash
python bot.py
```

Du siehst:
```
✦ SoulLight Bot gestartet! ✦
```

Der Bot läuft jetzt! Öffne Telegram und schreibe deinem Bot `/start` 🎉

---

## 📁 Projektstruktur

```
bot/
├── bot.py              ← Haupteinstiegspunkt (starten mit: python bot.py)
├── config.py           ← Lädt Einstellungen aus .env
├── data.py             ← Alle Inhalte (Affirmationen, Meditationen, FAQ, etc.)
├── handlers.py         ← Alle Bot-Commands & Button-Handler
├── scheduler.py        ← Automatische tägliche Aufgaben
├── requirements.txt    ← Python-Pakete
├── .env.example        ← Vorlage für Konfiguration
└── README.md           ← Diese Datei
```

---

## 🔧 Bot 24/7 laufen lassen

### Option A: Eigener PC (einfach, aber PC muss an bleiben)
```bash
python bot.py
# Terminal offen lassen
```

### Option B: Kostenloser Server (empfohlen)

**Railway.app** (kostenlos zum Starten):
1. Gehe zu https://railway.app
2. Verbinde dein GitHub-Repository
3. Railway erkennt Python automatisch
4. Füge die `.env`-Variablen unter "Variables" hinzu
5. Deploy! 🚀

**Render.com** (kostenlos):
1. Gehe zu https://render.com
2. Neuer "Background Worker"
3. Verbinde GitHub → `bot/` Ordner
4. Start Command: `python bot.py`
5. Environment Variables eintragen

### Option C: VPS (für Fortgeschrittene)
```bash
# Auf einem Linux-Server (z.B. Hetzner ab 3,49€/Monat)
nohup python bot.py &
# oder mit systemd/pm2 für Auto-Restart
```

---

## 📌 Nächste Erweiterungen

- [ ] Stripe Webhook für automatische Premium-Freischaltung
- [ ] Google Sheets Integration für Kundendaten
- [ ] Termin-Erinnerungen (24h / 1h vor Session)
- [ ] Feedback-System nach Sessions
- [ ] Mondphasen-Kalender (automatische Vollmond/Neumond Posts)
- [ ] Audio-Dateien versenden (Meditationen als .mp3)

---

## 💜 Support

Bei Fragen zum Bot: hello@soullight-academy.de
