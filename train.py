from chatterbot import ChatBot
chatbot = ChatBot('helpdesk',trainer='chatterbot.trainers.ListTrainers')
chatbot.train([
    "Oi",
    "Olá",
    "Como você está?",
    "Eu estou bem e você?",
    "Bom ouvir isso",
    "Obrigado",
    "De nada"
])
chatbot.train([
    "Tchau!",
    "Vejo você mais tarde!"
])
