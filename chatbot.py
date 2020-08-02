#!/usr/bin/env python
#@author: Gustavo Guzmán

import os
from telegram.ext import Updater, MessageHandler, CommandHandler
from telegram.ext import ConversationHandler, Filters
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import yfinance as yf

# Global variables
token = os.environ["TOKEN"]
keyboard = [['SI', 'NO']]
reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard = True,
                                       resize_keyboard = True)
PORT = int(os.environ.get("PORT", 5000))

# Functions definition
def start(update, context):
    """
    The bot says hello to the user and ask him to continue or cancel the 
    conversation, displaying the keyboard.
    The process moves to choice function.
    """
    welcome_text = "Hola! Soy StockMarketAR. ¿Te interesa conocer la última " \
                   "cotización de alguna acción en los mercados de valores " \
                   "argentinos?"
    update.message.reply_text(welcome_text, reply_markup = reply_markup)
    return "CHOICE"

def choice (update, context):
    """
    The bot receives user's answer, removing the keyboard.
    If it is 'SI', the bot ask him stock's ticker and the process moves to 
    stock_query function.
    If not, the conversation ends.
    """
    answer = update.message.text
    user = update.message.from_user
    update.message.reply_text("Gracias por tu respuesta!",
                              reply_markup = ReplyKeyboardRemove())
    if answer == 'SI':
        update.message.reply_text("Por favor, indica el símbolo de la acción " \
                                  "(ticker) cuya cotización te interesa " \
                                  "conocer.")
        return "STOCK"
    else:
        ending_text = "Por el momento, solo puedo brindarte la última " \
                      "cotización de acciones.\nVuelve pronto, estoy " \
                      "aprendiendo a realizar otras tareas."
        update.message.reply_text(ending_text)
        return ConversationHandler.END
          
def stock_query(update, context):
    """
    The bot receives the ticker entered by the user and evaluates if it is in
    accion list.
    If it is, it displays last stock price and the process moves to choice
    function.
    if not, it asks him to enter the ticker one more time and stock_query 
    function is executed again.
    """
    stock_name = update.message.text
    stock_name = stock_name.upper()
    accion = [
        "AGRO",
        "ALUA",
        "AUSO",
        "BBAR",
        "BHIP",
        "BMA",
        "BOLT",
        "BPAT",
        "BRIO",
        "BYMA",
        "CADO",
        "CAPU",
        "CAPX",
        "CARC",
        "CECO2",
        "CELU",
        "CEPU",
        "CGPA2",
        "COME",
        "CRES",
        "CTIO",
        "CVH",
        "DGCU2",
        "DOME",
        "DYCA",
        "EDN",
        "ESME",
        "FERR",
        "FIPL",
        "GAMI",
        "GARO",
        "GBAN",
        "GCLA",
        "GGAL",
        "GRIM",
        "MIRG",
        "HARG",
        "HAVA",
        "INAG",
        "INDU",
        "INTR",
        "INVJ",
        "IRCP",
        "IRSA",
        "LEDE",
        "LOMA",
        "LONG",
        "MERA",
        "METR",
        "MIRG",
        "MOLA",
        "MOLI",
        "MORI",
        "OEST",
        "PAMP",
        "PATA",
        "PATY",
        "PGR",
        "POLL",
        "RICH",
        "RIGO",
        "ROSE",
        "SAMI",
        "SEMI",
        "SUPV",
        "TECO2",
        "TGLT",
        "TGNO4",
        "TGSU2",
        "TRAN",
        "TXAR",
        "VALO",
        "YPFD"
        ]
    if stock_name in accion:
        price = yf.download(
        f"{stock_name}"+".BA",
        period = "1d"
        )["Adj Close"][0]
        update.message.reply_text(f"La última cotización de {stock_name} es " \
                                  f"{price:.2f}\n¿Deseas consultar otra " \
                                  "cotización?",
                                  reply_markup = reply_markup)
        return "CHOICE"
    else:
        update.message.reply_text(f"{stock_name} no parece ser un símbolo " \
                                  "válido.\n¿Puedes ingresarlo otra vez?")
        return "STOCK"
        
def cancel(update, context):
    """
    The bot says goodbye and the conversation ends.
    """
    update.message.reply_text("Espero haberte ayudado. Hasta pronto!")
    return ConversationHandler.END
     
def main():
    """
    The main function includes deployment settings and conversation's flow
    settings.
    """
    updater = Updater(token, use_context = True)
    disp = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points = [CommandHandler('start', start)],
        states = {
            "CHOICE": [MessageHandler(Filters.text, choice)],
            "STOCK": [MessageHandler(Filters.text, stock_query)]
            },
        fallbacks = [CommandHandler('cancel', cancel)]
        )
    disp.add_handler(conv_handler)
    updater.start_webhook(listen = "0.0.0.0",
                          port = int(PORT),
                          url_path = token)
    updater.bot.setWebhook('https://appname.herokuapp.com/' + token)
    updater.idle()

if __name__ == '__main__':
    main()