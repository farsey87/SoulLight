"""
SoulLight Academy – Telegram Bot
Handler-Modul: Alle Command- und Callback-Handler
"""
import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from data import AFFIRMATIONEN, MEDITATIONEN, ANGEBOTE, PAKETE, FAQ
import config


# ╔═══════════════════════════════════════════╗
# ║            HILFSFUNKTIONEN                ║
# ╚═══════════════════════════════════════════╝

def hauptmenu_keyboard() -> InlineKeyboardMarkup:
    """Erzeugt das Hauptmenü als Inline-Keyboard."""
    keyboard = [
        [
            InlineKeyboardButton("🌀 Angebote", callback_data="menu_angebote"),
            InlineKeyboardButton("📦 Pakete", callback_data="menu_pakete"),
        ],
        [
            InlineKeyboardButton("📅 Termin buchen", callback_data="menu_buchen"),
            InlineKeyboardButton("⭐ Premium", callback_data="menu_premium"),
        ],
        [
            InlineKeyboardButton("🧘 Meditation", callback_data="menu_meditation"),
            InlineKeyboardButton("✨ Affirmation", callback_data="menu_affirmation"),
        ],
        [
            InlineKeyboardButton("❓ FAQ", callback_data="menu_faq"),
            InlineKeyboardButton("📞 Kontakt", callback_data="menu_kontakt"),
        ],
        [
            InlineKeyboardButton("🌐 Website besuchen", url=config.WEBSITE_URL),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def zurueck_keyboard() -> InlineKeyboardMarkup:
    """Button zurück zum Hauptmenü."""
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton("🏠 Hauptmenü", callback_data="menu_start")]]
    )


def angebote_detail_keyboard() -> InlineKeyboardMarkup:
    """Buttons für einzelne Angebote."""
    keyboard = [
        [InlineKeyboardButton(f"{v['emoji']} {v['titel']}", callback_data=f"angebot_{k}")]
        for k, v in ANGEBOTE.items()
    ]
    keyboard.append([InlineKeyboardButton("🏠 Hauptmenü", callback_data="menu_start")])
    return InlineKeyboardMarkup(keyboard)


def pakete_detail_keyboard() -> InlineKeyboardMarkup:
    """Buttons für einzelne Pakete."""
    keyboard = [
        [InlineKeyboardButton(f"{v['emoji']} {v['titel']} – {v['preis']}", callback_data=f"paket_{k}")]
        for k, v in PAKETE.items()
    ]
    keyboard.append([InlineKeyboardButton("🏠 Hauptmenü", callback_data="menu_start")])
    return InlineKeyboardMarkup(keyboard)


def buchen_keyboard() -> InlineKeyboardMarkup:
    """Buttons für Buchungs-Kategorien."""
    keyboard = [
        [InlineKeyboardButton(f"{v['emoji']} {v['titel']}", callback_data=f"buchen_{k}")]
        for k, v in ANGEBOTE.items()
    ]
    keyboard.append([InlineKeyboardButton("🏠 Hauptmenü", callback_data="menu_start")])
    return InlineKeyboardMarkup(keyboard)


def faq_keyboard() -> InlineKeyboardMarkup:
    """Buttons für FAQ-Fragen."""
    keyboard = [
        [InlineKeyboardButton(f"❓ {faq['frage']}", callback_data=f"faq_{i}")]
        for i, faq in enumerate(FAQ)
    ]
    keyboard.append([InlineKeyboardButton("🏠 Hauptmenü", callback_data="menu_start")])
    return InlineKeyboardMarkup(keyboard)


# ╔═══════════════════════════════════════════╗
# ║           COMMAND-HANDLER                 ║
# ╚═══════════════════════════════════════════╝

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """/start – Willkommensnachricht mit Hauptmenü."""
    user = update.effective_user
    text = (
        f"✦ *Willkommen bei SoulLight Academy, {user.first_name}!* ✦\n\n"
        "🌙 Dein Raum für spirituelle Heilung,\n"
        "Transformation und Seelenarbeit.\n\n"
        "Hier kannst du:\n"
        "🔮 Unsere Angebote entdecken\n"
        "📅 Sessions buchen\n"
        "🧘 Meditationen empfangen\n"
        "⭐ Der Premium-Community beitreten\n\n"
        "Wähle eine Option aus dem Menü:"
    )
    await update.message.reply_text(
        text, parse_mode="Markdown", reply_markup=hauptmenu_keyboard()
    )


async def angebote_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """/angebote – Übersicht der Dienstleistungen."""
    text = (
        "✦ *Unsere Angebote* ✦\n\n"
        "Wähle einen Bereich, um mehr zu erfahren:"
    )
    await update.message.reply_text(
        text, parse_mode="Markdown", reply_markup=angebote_detail_keyboard()
    )


async def pakete_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """/pakete – Premium-Pakete anzeigen."""
    text = (
        "✦ *Premium-Pakete* ✦\n\n"
        "Intensive Begleitung für deine Transformation.\n"
        "Wähle ein Paket für alle Details:"
    )
    await update.message.reply_text(
        text, parse_mode="Markdown", reply_markup=pakete_detail_keyboard()
    )


async def buchen_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """/buchen – Buchungsprozess starten."""
    text = (
        "📅 *Termin buchen*\n\n"
        "Welche Art von Session möchtest du buchen?"
    )
    await update.message.reply_text(
        text, parse_mode="Markdown", reply_markup=buchen_keyboard()
    )


async def meditation_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """/meditation – Zufällige Meditation senden."""
    med = random.choice(MEDITATIONEN)
    text = f"*{med['titel']}*\n\n{med['text']}"
    await update.message.reply_text(
        text, parse_mode="Markdown", reply_markup=zurueck_keyboard()
    )


async def affirmation_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """/affirmation – Zufällige Affirmation senden."""
    aff = random.choice(AFFIRMATIONEN)
    text = f"✦ *Deine Affirmation für den Moment:*\n\n{aff}"
    await update.message.reply_text(
        text, parse_mode="Markdown", reply_markup=zurueck_keyboard()
    )


async def faq_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """/faq – Häufig gestellte Fragen."""
    text = (
        "❓ *Häufig gestellte Fragen*\n\n"
        "Tippe auf eine Frage, um die Antwort zu sehen:"
    )
    await update.message.reply_text(
        text, parse_mode="Markdown", reply_markup=faq_keyboard()
    )


async def kontakt_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """/kontakt – Kontaktmöglichkeiten anzeigen."""
    text = (
        "📞 *Kontakt*\n\n"
        f"🌐 Website: {config.WEBSITE_URL}\n"
        "📧 E-Mail: hello@soullight-academy.de\n"
        "📱 Telegram: @SoulLightAcademy\n\n"
        "💬 Du kannst mir auch einfach hier eine "
        "Nachricht schreiben – ich antworte so schnell wie möglich!"
    )
    await update.message.reply_text(
        text, parse_mode="Markdown", reply_markup=zurueck_keyboard()
    )


async def premium_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """/premium – Infos zur Premium-Gruppe."""
    text = (
        "⭐ *SoulLight Inner Circle*\n"
        "Deine Premium-Community – 19€/Monat\n\n"
        "Was dich erwartet:\n"
        "• 🎧 Exklusive Healings & Voice-Messages\n"
        "• 🧘 Geführte Meditationen (2x/Woche)\n"
        "• 🔓 Live Mini-Clearing Sessions\n"
        "• ❓ Wöchentliche Q&A Runden\n"
        "• 🌙 Vollmond/Neumond Rituale\n"
        "• 💬 Persönliche Betreuung (Mo-Fr)\n"
        "• 🚀 Frühzeitiger Zugang zu neuen Angeboten\n\n"
        "✨ Jetzt beitreten und deine Transformation vertiefen!"
    )
    keyboard = []
    if config.STRIPE_LINK_PREMIUM:
        keyboard.append(
            [InlineKeyboardButton("💳 Jetzt beitreten (19€/Monat)", url=config.STRIPE_LINK_PREMIUM)]
        )
    keyboard.append([InlineKeyboardButton("🏠 Hauptmenü", callback_data="menu_start")])
    await update.message.reply_text(
        text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def hilfe_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """/hilfe – Alle verfügbaren Befehle anzeigen."""
    text = (
        "📋 *Alle Befehle:*\n\n"
        "/start – Hauptmenü anzeigen\n"
        "/angebote – Unsere Dienstleistungen\n"
        "/pakete – Premium-Pakete\n"
        "/buchen – Termin buchen\n"
        "/premium – Inner Circle beitreten\n"
        "/meditation – Geführte Meditation\n"
        "/affirmation – Tagesaffirmation\n"
        "/faq – Häufige Fragen\n"
        "/kontakt – Kontaktdaten\n"
        "/hilfe – Diese Übersicht"
    )
    await update.message.reply_text(
        text, parse_mode="Markdown", reply_markup=zurueck_keyboard()
    )


# ╔═══════════════════════════════════════════╗
# ║         CALLBACK-QUERY HANDLER            ║
# ╚═══════════════════════════════════════════╝

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Verarbeitet alle Inline-Keyboard Klicks."""
    query = update.callback_query
    await query.answer()
    data = query.data

    # ── Hauptmenü ──────────────────────────
    if data == "menu_start":
        user = update.effective_user
        text = (
            f"✦ *Willkommen zurück, {user.first_name}!* ✦\n\n"
            "Was möchtest du tun?"
        )
        await query.edit_message_text(
            text, parse_mode="Markdown", reply_markup=hauptmenu_keyboard()
        )

    # ── Menü-Weiterleitungen ───────────────
    elif data == "menu_angebote":
        text = "✦ *Unsere Angebote* ✦\n\nWähle einen Bereich:"
        await query.edit_message_text(
            text, parse_mode="Markdown", reply_markup=angebote_detail_keyboard()
        )

    elif data == "menu_pakete":
        text = (
            "✦ *Premium-Pakete* ✦\n\n"
            "Intensive Begleitung für deine Transformation:"
        )
        await query.edit_message_text(
            text, parse_mode="Markdown", reply_markup=pakete_detail_keyboard()
        )

    elif data == "menu_buchen":
        text = "📅 *Termin buchen*\n\nWelche Session möchtest du buchen?"
        await query.edit_message_text(
            text, parse_mode="Markdown", reply_markup=buchen_keyboard()
        )

    elif data == "menu_meditation":
        med = random.choice(MEDITATIONEN)
        text = f"*{med['titel']}*\n\n{med['text']}"
        await query.edit_message_text(
            text, parse_mode="Markdown", reply_markup=zurueck_keyboard()
        )

    elif data == "menu_affirmation":
        aff = random.choice(AFFIRMATIONEN)
        text = f"✦ *Deine Affirmation:*\n\n{aff}"
        await query.edit_message_text(
            text, parse_mode="Markdown", reply_markup=zurueck_keyboard()
        )

    elif data == "menu_faq":
        text = "❓ *Häufige Fragen*\n\nTippe auf eine Frage:"
        await query.edit_message_text(
            text, parse_mode="Markdown", reply_markup=faq_keyboard()
        )

    elif data == "menu_kontakt":
        text = (
            "📞 *Kontakt*\n\n"
            f"🌐 Website: {config.WEBSITE_URL}\n"
            "📧 E-Mail: hello@soullight-academy.de\n"
            "📱 Telegram: @SoulLightAcademy\n\n"
            "💬 Schreibe mir einfach eine Nachricht!"
        )
        await query.edit_message_text(
            text, parse_mode="Markdown", reply_markup=zurueck_keyboard()
        )

    elif data == "menu_premium":
        text = (
            "⭐ *SoulLight Inner Circle* – 19€/Monat\n\n"
            "• 🎧 Exklusive Healings & Voice-Messages\n"
            "• 🧘 Geführte Meditationen (2x/Woche)\n"
            "• 🔓 Live Mini-Clearing Sessions\n"
            "• ❓ Wöchentliche Q&A Runden\n"
            "• 🌙 Vollmond/Neumond Rituale\n"
            "• 💬 Persönliche Betreuung (Mo-Fr)"
        )
        keyboard = []
        if config.STRIPE_LINK_PREMIUM:
            keyboard.append(
                [InlineKeyboardButton("💳 Jetzt beitreten", url=config.STRIPE_LINK_PREMIUM)]
            )
        keyboard.append([InlineKeyboardButton("🏠 Hauptmenü", callback_data="menu_start")])
        await query.edit_message_text(
            text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # ── Einzelne Angebote ──────────────────
    elif data.startswith("angebot_"):
        key = data.replace("angebot_", "")
        if key in ANGEBOTE:
            a = ANGEBOTE[key]
            text = f"{a['emoji']} *{a['titel']}*\n\n{a['beschreibung']}"
            keyboard = [
                [InlineKeyboardButton("📅 Jetzt buchen", callback_data=f"buchen_{key}")],
                [InlineKeyboardButton("◀️ Alle Angebote", callback_data="menu_angebote")],
                [InlineKeyboardButton("🏠 Hauptmenü", callback_data="menu_start")],
            ]
            await query.edit_message_text(
                text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard)
            )

    # ── Einzelne Pakete ────────────────────
    elif data.startswith("paket_"):
        key = data.replace("paket_", "")
        if key in PAKETE:
            p = PAKETE[key]
            text = f"{p['emoji']} *{p['titel']}*\n💰 {p['preis']}\n\n{p['beschreibung']}"
            stripe_key = f"STRIPE_LINK_{key.upper()}"
            stripe_url = getattr(config, stripe_key, "")
            keyboard = []
            if stripe_url:
                keyboard.append(
                    [InlineKeyboardButton(f"💳 {p['titel']} buchen", url=stripe_url)]
                )
            keyboard.append(
                [InlineKeyboardButton("📅 Beratungsgespräch buchen", url=config.BOOKING_URL)]
            )
            keyboard.append(
                [InlineKeyboardButton("◀️ Alle Pakete", callback_data="menu_pakete")]
            )
            keyboard.append(
                [InlineKeyboardButton("🏠 Hauptmenü", callback_data="menu_start")]
            )
            await query.edit_message_text(
                text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard)
            )

    # ── Buchung ────────────────────────────
    elif data.startswith("buchen_"):
        key = data.replace("buchen_", "")
        if key in ANGEBOTE:
            a = ANGEBOTE[key]
            text = (
                f"📅 *{a['titel']} buchen*\n\n"
                f"{a['beschreibung']}\n\n"
                "Klicke unten, um deinen Wunschtermin zu wählen:"
            )
            booking_link = f"{config.BOOKING_URL}/{key}"
            keyboard = [
                [InlineKeyboardButton("🗓️ Termin wählen", url=booking_link)],
                [InlineKeyboardButton("◀️ Andere Session wählen", callback_data="menu_buchen")],
                [InlineKeyboardButton("🏠 Hauptmenü", callback_data="menu_start")],
            ]
            await query.edit_message_text(
                text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard)
            )

    # ── FAQ-Antworten ──────────────────────
    elif data.startswith("faq_"):
        idx = int(data.replace("faq_", ""))
        if 0 <= idx < len(FAQ):
            faq = FAQ[idx]
            text = f"❓ *{faq['frage']}*\n\n{faq['antwort']}"
            keyboard = [
                [InlineKeyboardButton("◀️ Alle Fragen", callback_data="menu_faq")],
                [InlineKeyboardButton("🏠 Hauptmenü", callback_data="menu_start")],
            ]
            await query.edit_message_text(
                text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard)
            )


# ╔═══════════════════════════════════════════╗
# ║     GRUPPEN-EVENTS (Willkommen etc.)      ║
# ╚═══════════════════════════════════════════╝

async def welcome_new_member(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Begrüßt neue Mitglieder in Telegram-Gruppen."""
    for member in update.message.new_chat_members:
        if member.is_bot:
            continue

        chat_id = update.effective_chat.id

        if chat_id == config.FREE_GROUP_ID:
            text = (
                f"🌙 *Willkommen in der SoulLight Familie, {member.first_name}!* ✨\n\n"
                "Schön, dass du hier bist. 💜\n\n"
                "Hier erwartet dich:\n"
                "🌅 Tägliche Affirmationen\n"
                "🧘 Wöchentliche Live-Meditationen\n"
                "💬 Austausch mit Gleichgesinnten\n\n"
                "Starte unseren Bot @SoulLightBot für Termine, "
                "Meditationen und mehr!\n\n"
                "Stelle dich gerne kurz vor – wir freuen uns auf dich! 🙏"
            )
        elif chat_id == config.PREMIUM_GROUP_ID:
            text = (
                f"⭐ *Willkommen im Inner Circle, {member.first_name}!* ✨\n\n"
                "Du hast den nächsten Schritt gemacht – wie wunderbar! 💜\n\n"
                "Hier bekommst du:\n"
                "🎧 Exklusive Voice-Healings\n"
                "🔓 Live-Clearing Sessions\n"
                "❓ Q&A Runden\n"
                "🌙 Mondrituale\n\n"
                "Ich freue mich, dich intensiver begleiten zu dürfen! 🙏"
            )
        else:
            text = f"✨ Willkommen, {member.first_name}! 💜"

        await update.message.reply_text(text, parse_mode="Markdown")


# ╔═══════════════════════════════════════════╗
# ║        FREITEXT-NACHRICHTEN               ║
# ╚═══════════════════════════════════════════╝

async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Reagiert auf Freitext-Nachrichten im Privat-Chat."""
    # Nur im Privat-Chat antworten
    if update.effective_chat.type != "private":
        return

    text = (
        "💜 Danke für deine Nachricht!\n\n"
        "Ich leite sie weiter und melde mich so schnell wie möglich.\n\n"
        "In der Zwischenzeit kannst du unser Menü nutzen:"
    )
    await update.message.reply_text(
        text, parse_mode="Markdown", reply_markup=hauptmenu_keyboard()
    )

    # Nachricht an Admin weiterleiten
    if config.ADMIN_USER_ID:
        user = update.effective_user
        forward_text = (
            f"📩 *Neue Nachricht von:*\n"
            f"Name: {user.first_name} {user.last_name or ''}\n"
            f"Username: @{user.username or 'keiner'}\n"
            f"ID: `{user.id}`\n\n"
            f"💬 {update.message.text}"
        )
        try:
            await context.bot.send_message(
                chat_id=config.ADMIN_USER_ID,
                text=forward_text,
                parse_mode="Markdown",
            )
        except Exception:
            pass  # Admin nicht erreichbar – stille Fehlerbehandlung
