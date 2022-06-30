import datetime
import wikipedia
import webbrowser

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging
logging.basicConfig(level=logging.CRITICAL)


def greeting():
	hour = int(datetime.datetime.now().hour)
	if hour>=0 and hour<=12:
		print("Bom dia")
	elif hour>=12 and hour<18:
		print("Boa tarde")
	else:
		print("Boa noite")
	print("Eu sou ubi. Como posso ajudar?")

def ending():
	hour = int(datetime.datetime.now().hour)
	if hour>=0 and hour<3 or hour>=20 and hour<=23:
		print("Vejo você amanha, boa noite")
	else:
		print("Tchau, tenha um bom dia")

def wiki(query):
	try:
		query = query.replace("wikipedia","")
		results = wikipedia.summary(query,sentences=2)
		print(*results)
		return True
	except:
		return False


# Create a new instance of a ChatBot
bot = ChatBot('helpdesk', storage_adapter='chatterbot.storage.SQLStorageAdapter')

trainer = ChatterBotCorpusTrainer(bot)

trainer.train("chatterbot.corpus.portuguese")

greeting()
user_input = input()
while user_input:
	if user_input=="tchau":
		ending()
		break
	bot_response = str(bot.get_response(user_input))
	if(bot_response=='Como você está?'):
		if(wiki(user_input)==False):
			print("Desculpe, eu não entendi isso.")
	else:
		print(bot_response)
	user_input = input()

