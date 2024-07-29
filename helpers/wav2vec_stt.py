# general house keeping
import warnings
warnings.filterwarnings('ignore')

# ------------------------------------------------------------------------------------
# audio to text pipeline
from transformers import Wav2Vec2Tokenizer, Wav2Vec2ForCTC
import librosa as lb
import torch


tokenizer = Wav2Vec2Tokenizer.from_pretrained('../models/tokenizer-speechbrain')   #loads facebook/wav2vec2-base-960h tokenizer
model = Wav2Vec2ForCTC.from_pretrained('../models/model-speechbrain')              #loads facebook/wav2vec2-base-960h tokenizer

def audiototext(wav_file_path, sampling_rate = 16000):
    waveform, rate = lb.load(wav_file_path, sr = sampling_rate)
    input_values = tokenizer(waveform, return_tensors='pt').input_values
    logits = model(input_values).logits
    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = tokenizer.batch_decode(predicted_ids)
    return str(transcription[0]).lower()