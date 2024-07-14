# general house keeping
import warnings
warnings.filterwarnings('ignore')

# ------------------------------------------------------------------------------------
# audio to text pipeline
from transformers import Wav2Vec2Tokenizer, Wav2Vec2ForCTC
import librosa as lb
import torch


tokenizer = Wav2Vec2Tokenizer.from_pretrained('models/tokenizer-speechbrain')   #loads facebook/wav2vec2-base-960h tokenizer
model = Wav2Vec2ForCTC.from_pretrained('models/model-speechbrain')              #loads facebook/wav2vec2-base-960h tokenizer

def audiototext(wav_file_path, sampling_rate = 16000):
    waveform, rate = lb.load(wav_file_path, sr = sampling_rate)
    input_values = tokenizer(waveform, return_tensors='pt').input_values
    logits = model(input_values).logits
    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = tokenizer.batch_decode(predicted_ids)
    return str(transcription[0]).lower()


# ------------------------------------------------------------------------------------
# text to audio pipeleine
import torchaudio
from speechbrain.inference.TTS import Tacotron2
from speechbrain.inference.vocoders import HIFIGAN
import os

# Intialize TTS (tacotron2) and Vocoder (HiFIGAN)
tacotron2 = Tacotron2.from_hparams(source="models/tacotron")
hifi_gan = HIFIGAN.from_hparams(source="models/hifigan")


def texttoaudio(text, out_filename = 'output.wav'):
    mel_output, mel_length, alignment = tacotron2.encode_text(text)
    waveforms = hifi_gan.decode_batch(mel_output)
    
    output_dir = "outputs"
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    file_name = out_filename
    torchaudio.save(file_name, waveforms.squeeze(1), 22050)
# ------------------------------------------------------------------------------------