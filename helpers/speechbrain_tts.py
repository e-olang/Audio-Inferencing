# general house keeping
import warnings
warnings.filterwarnings('ignore')

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