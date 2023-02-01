from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime
from chatterbot.trainers import ListTrainer
import wikipedia
import webbrowser
import os
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging
logging.basicConfig(level=logging.CRITICAL)

def greeting():
	hour = int(datetime.datetime.now().hour)
	if hour>=0 and hour<=12:
		bot_response="Bom dia. "
	elif hour>=12 and hour<18:
		bot_response="Boa tarde. "
	else:
		bot_response="Boa noite. "
	bot_response+="Eu sou Ubi. Como posso ajudar?"
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

def reset (usuario):
    os.system('sudo passwd ' + usuario) 
    print("Bot: Você já pode usar a nova senha!")

# Create a new instance of a ChatBot
bot = ChatBot('Helpdesk', storage_adapter='chatterbot.storage.SQLStorageAdapter')


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


def index(request):
	if request.method == "POST":
		print("yha aaya")
		message = request.POST["message"]
		message=message.lower()
		print(message)
		if message=="bye":
			bot_response=ending()
		elif message.find('senha') != -1:
		    bot_response="Digite a nova senha para o usuário"
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


