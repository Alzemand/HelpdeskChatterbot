from django.shortcuts import render,redirect
from django.http import HttpResponse
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging
logging.basicConfig(level=logging.CRITICAL)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
	engine.say(audio)
	# engine.runAndWait()

def greeting():
	hour = int(datetime.datetime.now().hour)
	if hour>=0 and hour<=12:
		bot_response="Good Morning. "
		# print("Good Morning")
		# speak("Good Morning")
	elif hour>=12 and hour<18:
		# print("Good Afternoon")
		# speak("Good Afternoon")
		bot_response="Good Afternoon. "
	else:
		# print("Good Evening")
		# speak("Good Evening")
		bot_response="Good Evening. "
	# speak("I am MyBot. How can I help you?")
	bot_response+="I am MyBot. How can I help you?"
	# print("I am MyBot. How can I help you?")
	# speak(bot_response)
	return bot_response

def ending():
	hour = int(datetime.datetime.now().hour)
	if hour>=0 and hour<3 or hour>=20 and hour<=23:
		print("Byee see you tomorrow. Good Night")
		bot_response="Byee see you tomorrow. Good Night"
		# speak("Byee see you tomorrow. Good Night")
	else:
		print("Bye. Have a good day")
		bot_response="Bye. Have a good day"
		# speak("Bye. Have a good day")
	return bot_response

def wiki(query):
	try:
		query = query.replace("wikipedia","")
		results = wikipedia.summary(query,sentences=2)
		# speak("Searching...")
		# speak("According to wikipedia")
		print(*results)
		# speak(results)
		return True
	except:
		return False


# Create a new instance of a ChatBot
bot = ChatBot('MyBot', storage_adapter='chatterbot.storage.SQLStorageAdapter')

trainer = ChatterBotCorpusTrainer(bot)

trainer.train("chatterbot.corpus.english")

def index(request):
	if request.method == "POST":
		print("yha aayaa")
		message = request.POST["message"]
		print(message)
		if message=="bye":
			bot_response=ending()
			print("hahs",bot_response)
		else:
			bot_response = str(bot.get_response(message))
			if(bot_response=='How are you?'):
				if(wiki(message)==False):
					bot_response="Sorry I didn't get it."
					print("Sorry I didn't get it.")
					# speak("Sorry I didn't get it.")
			else:
				print(bot_response)
				speak(bot_response)
		return HttpResponse(bot_response)
	else:
		bot_response=""
		response=greeting()
		print(response)
		return render(request,"index.html",{"response_greeting":response})

