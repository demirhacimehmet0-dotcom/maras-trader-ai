from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = 8965706861:"AAHq3aAHxOKmoXPc4qegmHRA5aSjvFxL0c8"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Maraş Trader AI Botu çalışıyor!"
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
