from playsound import playsound
from gtts import gTTS
import sys
from tika import parser
raw = parser.from_file('Vaibhav_Mishra_Resume.pdf')
play_text = raw['content']



audio = 'pdf_to_audio.mp3'
language = 'en'
clip = gTTS(text=play_text,lang=language,slow=False)
clip.save(audio)
playsound(audio)

