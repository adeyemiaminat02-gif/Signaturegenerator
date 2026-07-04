import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Signature styling function
def generate_signatures(text: str) -> str:
    styles = [
        f"✍️ 𝔖𝔦𝔤𝔫𝔞𝔱𝔲𝔯𝔢 1: {text}",
        f"✍️ 𝓢𝓲𝓰𝓷𝓪𝓽𝓾𝓻𝓮 2: {text}",
        f"✍️ 𝕊𝕚𝕘𝕟𝕒𝕥𝕦𝕣𝕖 𝟛: {text}",
        f"✍️ 🄲🄿🅈-🄿🄰🅂🅃🄴: {text}",
        f"✍️ ───※ {text} ※───"
    ]
    return "\n\n".join(styles)

# /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "👋 Welcome to the Signature Generator Bot!\n"
        "Just type any name or phrase, and I'll generate beautiful signatures for you."
    )

# Message handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_text = update.message.text
    signatures = generate_signatures(user_text)
    await update.message.reply_text(f"Here are your signature options:\n\n{signatures}")

def main():
    # Retrieve the token from environment variables (important for production!)
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    
    if not TOKEN:
        logger.error("No bot token found! Please set TELEGRAM_BOT_TOKEN.")
        return

    # Build the application
    application = Application.builder().token(TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start long polling
    logger.info("Bot is starting up...")
    application.run_polling()

if __name__ == '__main__':
    main()
