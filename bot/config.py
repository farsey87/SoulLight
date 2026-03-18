"""
SoulLight Academy – Konfiguration
Lädt alle Einstellungen aus der .env Datei
"""
import os
from dotenv import load_dotenv

load_dotenv()


# ── Bot ─────────────────────────────────────────
BOT_TOKEN: str = os.getenv("BOT_TOKEN", "")

# ── Gruppen ─────────────────────────────────────
FREE_GROUP_ID: int = int(os.getenv("FREE_GROUP_ID", "0"))
PREMIUM_GROUP_ID: int = int(os.getenv("PREMIUM_GROUP_ID", "0"))
VIP_GROUP_ID: int = int(os.getenv("VIP_GROUP_ID", "0"))

# ── Admin ───────────────────────────────────────
ADMIN_USER_ID: int = int(os.getenv("ADMIN_USER_ID", "0"))

# ── Links ───────────────────────────────────────
WEBSITE_URL: str = os.getenv("WEBSITE_URL", "https://farsey87.github.io/SoulLight")
BOOKING_URL: str = os.getenv("BOOKING_URL", "https://cal.com/soullight")

# ── Stripe ──────────────────────────────────────
STRIPE_LINK_PREMIUM: str = os.getenv("STRIPE_LINK_PREMIUM", "")
STRIPE_LINK_ERWACHEN: str = os.getenv("STRIPE_LINK_ERWACHEN", "")
STRIPE_LINK_BEFREIUNG: str = os.getenv("STRIPE_LINK_BEFREIUNG", "")
STRIPE_LINK_SEELENREISE: str = os.getenv("STRIPE_LINK_SEELENREISE", "")
