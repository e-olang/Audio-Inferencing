# house-keeping
import os
from dotenv import load_dotenv
import warnings
warnings.filterwarnings('ignore')

# telegram bot management
from telegram import Update
from telegram.ext import Updater, CallbackContext, MessageHandler, Filters, CommandHandler, ConversationHandler
from pydub import AudioSegment
import pydub

# audio & LLM(Gemini Pro) inferencing
from audio_inference import audiototext, texttoaudio
from gemini_inference import respond


# ------------------------------------------------------------------------------------------------
load_dotenv()
telegram = os.getenv('TELEGRAM')
# ------------------------------------------------------------------------------------------------


# Define states for the conversation
WELCOME, VOICE = range(2)

def start(update: Update, context: CallbackContext) -> int:
    update.message.reply_text('Welcome! Please record and send a short audio question using the voice note feature.')
    return VOICE

def get_voice(update: Update, context: CallbackContext) -> int:
    update.message.reply_text('Voice note received. Processing...')
    # Download the voice note
    new_file = context.bot.get_file(update.message.voice.file_id)
    new_file.download("voice_note.ogg")
    
    # Notify the user that the voice note is being processed
    update.message.reply_text('Voice note being processed')

    # ------------------------------------------------------------------
    # Convert the OGG file to Waveform (WAV)
    audio = AudioSegment.from_ogg("voice_note.ogg")
    audio.export("voice_note.wav", format="wav")
    
    # ------------------------------------------------------------------
    # LLM Inferencing + Audio Production
    query_text = audiototext('voice_note.wav')
    LLM_response = respond(query_text)
    texttoaudio(LLM_response, 'voice_note.wav')
    
    # ------------------------------------------------------------------
    # Send the converted audio file back to the user
    with open("voice_note.wav", "rb") as audio_file:
        context.bot.send_voice(chat_id=update.message.chat_id, voice=audio_file)

    # Optionally, send another text message
    # update.message.reply_text('Response Message')

    # Clean up the files
    os.remove("voice_note.ogg")
    #os.remove("voice_note.wav")
    
    return ConversationHandler.END

def cancel(update: Update, context: CallbackContext) -> int:
    update.message.reply_text('Goodbye!')
    return ConversationHandler.END

# Set up the updater and dispatcher
updater = Updater(telegram)


conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        WELCOME: [MessageHandler(Filters.text & ~Filters.command, start)],
        VOICE: [MessageHandler(Filters.voice, get_voice)]
    },
    fallbacks=[CommandHandler('cancel', cancel)]
)
#print('Active')

updater.dispatcher.add_handler(conv_handler)

updater.start_polling()
updater.idle()