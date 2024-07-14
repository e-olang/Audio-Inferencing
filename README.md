# Audio-Inferencing: 
*Telegram Voice Note Bot for LLM Inferencing*

### Overview
This repository contains a Telegram bot that captures voice notes sent by users, transcribes them to text, infers a response using a Large Language Model (LLM) like Gemini Pro, and responds back with a voice note.

###  Architecture
The system consists of the following components:
- Telegram Bot: 
	- Receives voice notes from users.
	- Response: The generated voice note is sent back to the user via the bot.
- Voice Note to Text: The received voice note is transcribed to text using [insert STT model/library, e.g. Google Cloud Speech-to-Text, Mozilla DeepSpeech].
- LLM Inference: The transcribed text is passed to the Gemini Pro LLM for inference.
Text to Voice Note: The output of the LLM is converted to a voice note using [insert TTS model/library, e.g. Google Text-to-Speech, Amazon Polly].




### Implementation

The implementation is written in [insert programming language, e.g. *Python 3.9.19* and uses the following libraries:
``` python
	transformers
	python-dotenv
	torch
	torchaudio
	google-generativeai==0.7.2
	librosa==0.10.2.post1
	python-telegram-bot==13.15
	speechbrain
	torchvision
	pydub
```

### Usage

To use this application, follow these steps:

1.  Clone the repository and install the [required dependencies](requrements.txt).
2.  Run the application using  `python telegram_v1.py`  in your terminal or command prompt.
3.  Access the Telegram bot via the provided [link](https://t.me/sitol_bot). "https://t.me/sitol_bot"
4.  Send a voice note to the bot to initiate a conversation.
---
#### General manual/guide
1. Step 1: Install Telegram from Playstore (This bot is yet to be tested on the IOs Platform).
2. Step 2: Access bot via provided link and tap/click start at the bottom of the screen.
<div style="text-align: center;">
<img src="assets/telegram-1.jpg" width="200">
</div>
3. Step 3: **Hold** the mic icon (button) (botom right) to record and send a message. Pro-tip, start recording a message as soon as the mic button is held.
<div style="text-align: center;">
<img src="assets/telegram-2.jpg" width="200">
</div>
<br>
<div style="text-align: center;">
<img src="assets/telegram-3.jpg" alt="Description" width="200">
</div>


---

####  Future Work

|Task        					    |Description                    		            |Status|
|-----------------------------------|---------------------------------------            |-----------|
|Improve audio cleaning    			|`Resolve background noise issues`   	            |Ongoing    |
|Migrate to Faster Whisper  for STT	|`For multilingual caps`            	            |Ongoing    |
|Resolve Audio cut issue	        |`Sometimes audio sent back is cuat at 10s`         |Not-Started|
|Integratw Whatsapp Platoform       |										            |Not-Started|        
|Test on other LLMs :Ulizamama, etc	|										            |Not-Started|




#### License
This repository is licensed under **TBD**

 --- 

### Other:

#### Tests
- STT  Tests:

#### Dir Structure:
- Audio Inferencing
    - `assets/`             : Contains general media files for repo documentation
    - `models/`             : Contains model bin/safetensor/ckpt files (only for open source models)
    - `Notebooks/`          : Traning and Draft Jupyter notebooks
    - `outputs`             : Temp loaction for inspeiong wav, mp3 & ogg files during tests
    - `pretrained_models/`  : Contains model configuration files (only for open source models)
    - `run_files`           : Temp location for storing bot meida files during telegram inferencing
    - `samples`             : Sample audion files (wav, mp3, flac & ogg)






