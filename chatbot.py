#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# ubi virtual assistant
#
# Copyleft (C) 2016 Edilson Alzemand
# edilson_alzemand@id.uff.br
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import speech_recognition as sr 
from gtts import gTTS
from playsound import playsound 

def ouvir_microfone():
    frase = ''
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source, duration=1)
        print("ubi: Microfone ativo...")
        audio=microfone.listen(source)
    try:
        frase = microfone.recognize_google(audio, language='pt-BR')
        print("humano: ", frase)
    except sr.UnknownValueError:
        print("ubi: Isso não funcionou")
    return frase

def cria_audio(audio):
    tts = gTTS(audio, lang='pt-BR')
    tts.save('ubi.mp3')
    playsound('ubi.mp3')


bot = ChatBot("Ubi",
              storage_adapter='chatterbot.storage.SQLStorageAdapter',
              database_uri='sqlite:///ubi.sqlite3'
              )
			  
conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

trainer = ListTrainer(bot)

trainer.train(conversation)

# while True:
#     quest = ouvir_microfone()
#     resposta = bot.get_response(quest)
#     cria_audio(str(resposta))
#     print('Ubi: ', resposta)

while True:
	quest = input('humano: ')
	resposta = bot.get_response(quest)
	if float(resposta.confidence) > 0.5:
		print('Ubi: ', resposta)
	else:
		print('ubi: Não entendi')

