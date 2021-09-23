import telebot

CHAVE_API = "chave aqui"

bot = telebot.TeleBot(CHAVE_API)


@bot.message_handler(commands=["Descarga"])
def Descarga(mensagem):
    bot.send_message(mensagem.chat.id, "Vish, vou dar")

@bot.message_handler(commands=["Toalha"])
def Toalha(mensagem):
    bot.send_message(mensagem.chat.id, "Foi mal, vou estender jaja.")

@bot.message_handler(commands=["Remedio"])
def Remedio(mensagem):
    bot.send_message(mensagem.chat.id, "Esqueci de tomar, obrigado por lembrar!")



@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    texto = """
    O que deseja pedir? (Clique em um dos itens)
    /Descarga Dar a descarga no banheiro
    /Toalha Estenda a toalha depois do banho
    /Remedio tome o remedio"""
    bot.send_message(mensagem.chat.id, texto)
    

@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, "Muito obrigado! fico feliz em ouvir isso.")

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id, "Tudo bem! se precisar estou aqui.")




def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha o que quer fazer? (Clique no item)
    /opcao1 Pedir algo
    /opcao2 Me agradecer
    /opcao3 Nada
    Responder qualquer outra coisa nao vai funcionar, clique em uma das opcoes."""
    bot.reply_to(mensagem, texto)

bot.polling()
