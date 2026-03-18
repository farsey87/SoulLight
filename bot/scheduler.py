"""
SoulLight Academy – Scheduler
Automatische Aufgaben: Tägliche Affirmation, Session-Erinnerungen
"""
import random
import logging
from datetime import time
from telegram.ext import ContextTypes
from data import AFFIRMATIONEN
import config

logger = logging.getLogger(__name__)


async def taeglich_affirmation(context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Wird jeden Morgen um 7:00 Uhr ausgeführt.
    Sendet eine zufällige Affirmation in die kostenlose Gruppe.
    """
    if not config.FREE_GROUP_ID:
        return

    affirmation = random.choice(AFFIRMATIONEN)
    text = (
        "🌅 *Guten Morgen, SoulLight Familie!*\n\n"
        f"{affirmation}\n\n"
        "💜 Starte deinen Tag mit dieser Energie.\n"
        "Atme tief ein … und lass sie wirken. ✨"
    )
    try:
        await context.bot.send_message(
            chat_id=config.FREE_GROUP_ID,
            text=text,
            parse_mode="Markdown",
        )
        logger.info("✅ Tägliche Affirmation gesendet")
    except Exception as e:
        logger.error(f"❌ Affirmation senden fehlgeschlagen: {e}")


async def premium_impuls(context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Wird jeden Morgen um 8:00 Uhr ausgeführt.
    Sendet einen exklusiven Heilimpuls in die Premium-Gruppe.
    """
    if not config.PREMIUM_GROUP_ID:
        return

    impulse = [
        "🔮 *Tagesimpuls:* Lege heute bewusst deine Hand auf dein Herzchakra und sage 3x: 'Ich bin Liebe. Ich bin Licht. Ich bin frei.'",
        "🌿 *Tagesimpuls:* Gehe heute für 10 Minuten barfuß in der Natur. Spüre die Erdung und lasse alle Fremdenergie los.",
        "✨ *Tagesimpuls:* Zünde heute eine Kerze an und setze eine Intention für deine Heilung. Schreibe sie auf und lege sie unter die Kerze.",
        "🌙 *Tagesimpuls:* Bevor du heute schlafen gehst, sage: 'Ich bitte meine Seelenführer, mir im Schlaf Heilung und Klarheit zu schenken.'",
        "💜 *Tagesimpuls:* Trinke heute ein Glas Wasser und stelle dir vor, wie es mit goldenem Licht gefüllt ist. Jeder Schluck heilt dich von innen.",
        "🦋 *Tagesimpuls:* Schließe die Augen und frage dich: Welches Gefühl möchte heute gesehen werden? Gib ihm Raum.",
        "🕯️ *Tagesimpuls:* Räuchere heute deinen Raum mit Salbei oder Palo Santo. Sage: 'Nur Liebe und Licht dürfen hier sein.'",
    ]
    text = random.choice(impulse)

    try:
        await context.bot.send_message(
            chat_id=config.PREMIUM_GROUP_ID,
            text=text,
            parse_mode="Markdown",
        )
        logger.info("✅ Premium-Impuls gesendet")
    except Exception as e:
        logger.error(f"❌ Premium-Impuls fehlgeschlagen: {e}")


def schedule_jobs(job_queue) -> None:
    """Registriert alle geplanten Aufgaben im JobQueue."""

    # Tägliche Affirmation um 07:00 Uhr (deutsche Zeit, UTC+1/+2)
    job_queue.run_daily(
        taeglich_affirmation,
        time=time(hour=5, minute=0, second=0),  # 05:00 UTC = 07:00 MEZ
        name="daily_affirmation",
    )

    # Premium-Impuls um 08:00 Uhr
    job_queue.run_daily(
        premium_impuls,
        time=time(hour=6, minute=0, second=0),  # 06:00 UTC = 08:00 MEZ
        name="daily_premium_impuls",
    )

    logger.info("📅 Scheduler gestartet – Tägliche Jobs registriert")
