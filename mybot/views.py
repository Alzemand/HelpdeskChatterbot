from django.shortcuts import render,redirect
from django.http import HttpResponse
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import git
from django.views.decorators.csrf import csrf_exempt

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging
logging.basicConfig(level=logging.CRITICAL)

# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# engine.setProperty('voice',voices[0].id)

# def speak(audio):
# 	engine.say(audio)
	# engine.runAndWait()

@csrf_exempt
def update(request):
	if request.method=="POST":
		repo=git.Repo("muskan0210.pythonanywhere.com/")
		origin=repo.remotes.origin
		origin.pull()
		return HttpResponse("Updated")
	else:
		return HttpResponse("Couldn't update")


def greeting():
	hour = int(datetime.datetime.now().hour)
	if hour>=0 and hour<=12:
		bot_response="Good Morning. "
	elif hour>=12 and hour<18:
		bot_response="Good Afternoon. "
	else:
		bot_response="Good Evening. "
	bot_response+="I am MyBot. How can I help you?"
	return bot_response

def ending():
	hour = int(datetime.datetime.now().hour)
	if hour>=0 and hour<3 or hour>=20 and hour<=23:
		print("Byee see you tomorrow. Good Night")
		bot_response="Byee see you tomorrow. Good Night"
	else:
		print("Bye. Have a good day")
		bot_response="Bye. Have a good day"
	return bot_response

def wiki(query):
	try:
		query = query.replace("wikipedia","")
		results = wikipedia.summary(query,sentences=2)
		print(*results)
		return results
	except:
		return False


# Create a new instance of a ChatBot
bot = ChatBot('MyBot', storage_adapter='chatterbot.storage.SQLStorageAdapter')

trainer = ChatterBotCorpusTrainer(bot)

trainer.train("chatterbot.corpus.english")

def index(request):
	if request.method == "POST":
		message = request.POST["message"]
		message=message.lower()
		if message=="bye":
			bot_response=ending()
		elif message=="what is your name" or message=="who are you":
		    bot_response="My name is MyBot. I am a Robo."
		else:
			if(message[:4]=='what' or message[:3]=='who'):
				if(wiki(message)==False):
					bot_response="Sorry, I didn't get it."
					print("Sorry, I didn't get it.")
				else:
				    bot_response=wiki(message)
			else:
			    bot_response = str(bot.get_response(message))
		return HttpResponse(bot_response)
	else:
		bot_response=""
		response=greeting()
		print(response)
		return render(request,"index.html",{"response_greeting":response})

