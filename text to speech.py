from gtts import gTTS
import os

text_A='from gtta import gtts, import OS, language=english, os.system start text1.mp3'
language = 'en'

obj = gTTS(text=text_A, lang =language,slow = False)


obj.save('text1.mp3')

os.system('start text1.mp3')
