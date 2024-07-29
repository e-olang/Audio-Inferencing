# telegram bot management
from telegram import Update
from telegram.ext import Updater, CallbackContext, MessageHandler, Filters

# audio & LLM(Gemini Pro) inferencing
from helpers import gemini_inference, whisper_stt, elevenlabs_tts
import helpers.speechbrain_tts as speechbrain_tts

import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TELEGRAM')


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hello! Send me an audio message.')

def audio_message(update: Update, context: CallbackContext):
    # Get the audio file from the message
    audio_file = update.message.voice.get_file()
    audio_file.download('run_files/voice_note.wav')

    # Process the audio file using Whisper, Gemini, and SpeechBrain
    query_text = whisper_stt.audiototext('run_files/voice_note.wav')
    LLM_response = gemini_inference.respond(query_text)
    #speechbrain_tts.texttoaudio(LLM_response, 'run_files/voice_note.wav')
    elevenlabs_tts.texttoaudio(LLM_response, 'run_files/voice_note.wav')

    # Send the generated audio message back to the user
    context.bot.send_audio(chat_id=update.effective_chat.id, audio=open('run_files/voice_note.wav', 'rb'))

def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.voice, audio_message))
    dp.add_handler(MessageHandler(Filters.command('start'), start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()