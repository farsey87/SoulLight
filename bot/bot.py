"""
╔═══════════════════════════════════════════════════╗
║   ✦ SoulLight Academy – Telegram Bot ✦           ║
║   Spirituelle Heilung & Transformation            ║
║                                                   ║
║   Starte mit:  python bot.py                      ║
╚═══════════════════════════════════════════════════╝
"""
import logging
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters,
)
import config
from handlers import (
    start_command,
    angebote_command,
    pakete_command,
    buchen_command,
    meditation_command,
    affirmation_command,
    faq_command,
    kontakt_command,
    premium_command,
    hilfe_command,
    button_handler,
    welcome_new_member,
    text_handler,
)
from scheduler import schedule_jobs

# ── Logging ─────────────────────────────────────────
logging.basicConfig(
    format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger("SoulLightBot")


def main() -> None:
    """Bot starten."""
    if not config.BOT_TOKEN or config.BOT_TOKEN == "DEIN_BOT_TOKEN_HIER":
        logger.error(
            "❌ Kein Bot-Token gesetzt!\n"
            "   1. Erstelle einen Bot bei @BotFather auf Telegram\n"
            "   2. Kopiere .env.example → .env\n"
            "   3. Trage deinen Token in .env ein\n"
        )
        return

    # ── App erstellen ───────────────────────────────
    app = Application.builder().token(config.BOT_TOKEN).build()

    # ── Command-Handler ─────────────────────────────
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("angebote", angebote_command))
    app.add_handler(CommandHandler("pakete", pakete_command))
    app.add_handler(CommandHandler("buchen", buchen_command))
    app.add_handler(CommandHandler("meditation", meditation_command))
    app.add_handler(CommandHandler("affirmation", affirmation_command))
    app.add_handler(CommandHandler("faq", faq_command))
    app.add_handler(CommandHandler("kontakt", kontakt_command))
    app.add_handler(CommandHandler("premium", premium_command))
    app.add_handler(CommandHandler("hilfe", hilfe_command))
    app.add_handler(CommandHandler("help", hilfe_command))

    # ── Inline-Keyboard Callbacks ───────────────────
    app.add_handler(CallbackQueryHandler(button_handler))

    # ── Neue Mitglieder begrüßen ────────────────────
    app.add_handler(
        MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome_new_member)
    )

    # ── Freitext-Nachrichten (Privat-Chat) ──────────
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, text_handler)
    )

    # ── Geplante Aufgaben starten ───────────────────
    schedule_jobs(app.job_queue)

    # ── Bot starten ─────────────────────────────────
    logger.info("✦ SoulLight Bot gestartet! ✦")
    logger.info(f"  Website: {config.WEBSITE_URL}")
    logger.info(f"  Admin-ID: {config.ADMIN_USER_ID}")
    logger.info("  Drücke Strg+C zum Beenden.")

    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
