# house-keeping
import os
from dotenv import load_dotenv
import warnings


warnings.filterwarnings('ignore')

# telegram bot management
from telegram import Update
from telegram.ext import Updater, CallbackContext, MessageHandler, Filters
from pydub import AudioSegment
import pydub

# audio & LLM(Gemini Pro) inferencing
from helpers import gemini_inference, whisper_stt
import helpers.speechbrain_tts as speechbrain_tts


# ------------------------------------------------------------------------------------------------
load_dotenv()
telegram = os.getenv('TELEGRAM')
# ------------------------------------------------------------------------------------------------


def get_voice(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(':-)')
    # Download the voice note
    new_file = context.bot.get_file(update.message.voice.file_id)
    new_file.download("run_files/voice_note.ogg")
    
    # Notify the user that the voice note is being processed
    update.message.reply_text('Voice note being processed')

    # ------------------------------------------------------------------
    # Convert the OGG file to Waveform (WAV)
    audio = AudioSegment.from_ogg("run_files/voice_note.ogg")
    audio.export("run_files/voice_note.wav", format="wav")
    
    # ------------------------------------------------------------------
    # LLM Inferencing + Audio Production
    query_text = whisper_stt.audiototext('run_files/voice_note.wav')
    LLM_response = gemini_inference.respond(query_text)
    speechbrain_tts.texttoaudio(LLM_response, 'run_files/voice_note.wav')
    
    # ------------------------------------------------------------------
    # Send the converted audio file back to the user
    with open("run_files/voice_note.wav", "rb") as audio_file:
        context.bot.send_voice(chat_id=update.message.chat_id, voice=audio_file)
    
    # Optionally, send another text message
    update.message.reply_text('You can now send another query')

    # Clean up the files
    os.remove("run_files/voice_note.ogg")
    os.remove("run_files/voice_note.wav")


updater = Updater(telegram)

updater.dispatcher.add_handler(MessageHandler(Filters.voice , get_voice))

updater.start_polling()
updater.idle()